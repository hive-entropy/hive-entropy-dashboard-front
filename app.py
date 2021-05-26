#from flask import Flask, request, render_template, url_for, redirect, jsonify, json
from flask import *
import request as rqt

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        if 'nodeid' in request.form:
            nodeid = request.form['nodeid']
            print("info for nodeid " + nodeid)
            return redirect(url_for("nodeinfo", nodeid=nodeid))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/nodes',methods=['GET','POST'])
def nodes():
    nodes_dict = {}
    nodes_dict["gridData"] = rqt.get_nodes()
    nodes_dict["gridColumns"] = list(nodes_dict["gridData"][0].keys())
    #nodes_dict["nodesId"] = [d['id'] for d in nodes_dict["gridData"] if 'id' in d]
    print(nodes_dict)
    return json.dumps(nodes_dict)

@app.route("/nodes/<nodeid>/info")
def get_node_info(nodeid):
    info_node_dict={}
    info_node_dict["gridData"] = rqt.get_node_info(nodeid)
    info_node_dict["gridColumns"] = list(info_node_dict["gridData"].keys())
    info_node_dict["id"] = nodeid
    return json.dumps(info_node_dict)
    #return f "<h1>{nodeid}</h1>"

@app.route("/nodes/<nodeid>")
def node_info(nodeid):
    info_node_dict={}
    info_node_dict["gridData"] = rqt.get_node_info(nodeid)
    info_node_dict["gridColumns"] = list(info_node_dict["gridData"].keys())
    info_node_dict["id"] = nodeid
    return render_template('node_info.html',nodeid = nodeid,info_node_dict = json.dumps(info_node_dict) )

@app.route("/nodes/<nodeid>/deploy")
def node_deploy(nodeid):
    done = rqt.deploy_node(nodeid)
    #return render_template('node_info.html')
    return render_template('node_info.html',nodeid = nodeid, deploy_done = done)

if __name__ == "__main__":
    app.run(port=5000,debug=True)