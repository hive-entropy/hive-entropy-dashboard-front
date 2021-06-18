<template>
<div class="container">
 <div class="row">
    <h3>Nodes : </h3>
	<div class="col-11">
	<table class="table">
	<thead>
		<tr>
			<th scope="col">ID</th>
			<th scope="col">Address IP</th>
			<th scope="col">Architecture</th>
			<th scope="col">Proxy</th>
			<th scope="col">State</th>
		</tr>
	</thead>
	<tbody>
		<tr class="node-info-line" v-for="node in nodes" v-bind:key="node.id" v-on:click="get_infos($event)" v-bind:id="node.id">
		<!--onclick="document.location.href='#nodes_info';"-->
			<th scope="row">{{ node.id }}</th>
			<td>{{ node.address }}</td>
			<td>{{ node.arch }}</td>
			<td>{{ node.proxy }}</td>
			<td>{{ node.state }}</td>
		<!--v-on:click="deploy_node($event)"-->
		</tr>

	</tbody>
	</table>
	</div>
	<div class="col col-lg-1">
            <div style="margin-top: 45px;">
		<button style="margin:5px;" v-for="node in nodes" v-bind:key="node.id" v-on:click="changed" v-bind:id="'btn_'+ node.id">Start</button>
            </div>
	</div>
 </div>

  
 <div class="row">
	<p>{{ deploy_error }}</p>
	<h3 style="margin-top:50px">Information about node id : {{ selected_node.ID }}</h3>
	<table class="table" style="border-bottom-width: 1px;">
            <tr v-for="(key, item) in selected_node" v-bind:key="item" class="border_bottom">
		<th>{{ item }}</th>
		<td v-if="item==='processor'">
			<ul>
                           <li v-for="(val,cat) in key" v-bind:key="cat">
				<template v-if="cat==='frequency'">{{ cat }} : 
                                   <ul>
					<li v-for="(val2,cat2) in val" v-bind:key="cat2">{{ cat2 }} : {{ val2 }}
					</li>
                                   </ul>
				</template>
				<template v-else>
					{{ cat }} : {{ val }}
				</template>
                           </li>
			</ul>
		</td>
		<td v-else-if="item==='ram'">
			<ul>
                           <li v-for="(val,cat) in key" v-bind:key="cat">
				<template v-if="cat==='capacity'">{{ cat }} : 
                                   <ul>
					<li v-for="(val2,cat2) in val" v-bind:key="cat2">{{ cat2 }} : {{ val2 }}
					</li>
                                   </ul>
				</template>
				<template v-else>
					{{ cat }} : {{ val }}
				</template>
                           </li>
			</ul>
		</td>
		<td v-else>
			{{ key }}
		</td>
            </tr>
	</table>
 </div>

 <div class='row'>
	<h3 style="margin-top:50px">Information about logs :</h3>
	<div style="margin-left:50px; text-align:left">
            <p>{{ logs }}</p>
	</div>
 </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Nodes',
    data() {
      return {
        nodes: null,
        infos: null,
        selected_node : '',
        deploy_error : null
      };
    },
    created: function() {
      axios
        .get('http://sevenmoor.com:4444/nodes', this.data,{
        headers: {'Access-Control-Allow-Origin': '*'}
        })
        .then(res => {
          this.nodes = res.data;
        })
    },
    methods: {
     get_infos : function(event){
	var targetId = event.currentTarget.id;
	axios
	.get('http://sevenmoor.com:4444/nodes/'+targetId)
	.then(response => (this.selected_node = response.data))
	.catch(error => console.log(error))
     },
     changed : function(event) {
	var targetId = event.currentTarget.id;
	const nodeId = targetId.split('_')[1];
	alert(nodeId);
	if (event.target.textContent == "Stop"){
		this.node_start_stop(nodeId,"start")
		event.target.textContent = "Start"
		
	}
	else{
		this.node_start_stop(nodeId,"stop")
		event.target.textContent = "Stop"
		
	}
     },
     get_logs : function(event){
      var targetId = event.currentTarget.id;
      axios
	.get('http://sevenmoor.com:4444/nodes/'+targetId+'/logs')
	.then(response => (this.logs = JSON.stringify(response)))
	.catch(error => console.log(error))
     },
     deploy_node : function () {
	var targetId = event.currentTarget.id;
	var action = this.state_message
	axios
	.post('http://sevenmoor.com:4444/nodes/'+targetId+'/'+action.toLowerCase())
	.then(response => (this.deploy_error = response))
	.catch(error => console.log(error))
     },
     node_start_stop : async function (nodeId,action) {
	const response = await axios.post('http://sevenmoor.com:4444/nodes/' + nodeId + '/' + action.toLowerCase());
	alert(response);
     },
     intervalFetchData: function () {
     setInterval(() => {
        this.get_infos();
        }, 10000);
     }
    },
    mounted () {
        // Run the functions once when mounted 
        this.get_infos();
        // Run the intervalFetchData function once to set the interval time for later refresh
        this.intervalFetchData();
    }
}
</script>

<style>
    h3 {
	margin-bottom: 5%;
    }
</style>
