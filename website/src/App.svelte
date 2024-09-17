<script lang="ts">
	import { onMount } from "svelte";
	import "./app.css";
	import Header from "./components/Header.svelte";

	import * as myc from "@apple/mycelium";
	import "@apple/mycelium/dist/style.css";

	let el: HTMLDivElement;
	let viewer: myc.NetworkViewer;
	onMount(async () => {
		const d = await loadGraphData();
		const network = new myc.Network();
		setGraph(network, d);
		viewer = myc.NetworkViewer.create(network, el, {
			showBreadcrumbs: true,
			minimap: true,
		});
	});

	function setGraph(network: myc.Network, data: GraphData) {
		// set nodes
		for (let i = 0; i < data.nodes.length; i++) {
			const nodeId = data.nodes[i];
			const node = createNode(nodeId);
			network.setNode(nodeId, node);
		}

		// set edges
		for (let i = 0; i < data.edges.length; i++) {
			const edge = data.edges[i];
			if (edge[2] === 1) {
				network.setEdge(edge[0], edge[1]);
			}
		}
	}

	function createNode(nodeId: any) {
		return new myc.ui.Node(
			nodeId,
			new myc.ui.VStack(
				new myc.ui.Text("Node").with({ fontWeight: 600 }),
				new myc.ui.Text(nodeId)
			)
		);
	}

	interface GraphData {
		nodes: string[];
		edges: unknown[][];
	}

	async function loadGraphData() {
		const d = await fetch("shared/test.json");
		const j = await d.json();
		return j as GraphData;
	}
</script>

<Header />
<main>
	<div
		bind:this={el}
		style="width: 100vw; height: 800px; outline: 1px solid red;"
	/>
</main>

<style>
</style>
