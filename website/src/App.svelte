<script lang="ts">
	import { onMount } from "svelte";
	import "./app.css";
	import Header from "./components/Header.svelte";
	import Graph from "./components/Graph.svelte";
	import type { Link, Node } from "./types";
	import { Backend } from "./backend";

	let d: GraphData;
	let links: Link[] = [];
	let nodes: Node[] = [];
	onMount(async () => {
		d = await loadGraphData();
		const res = convertFormat(d);
		links = res[0];
		nodes = res[1];

		const out = await Backend.withinSimilar();
		console.log(out);
	});

	interface GraphData {
		nodes: string[];
		edges: unknown[][];
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

	function convertFormat(data: GraphData): [Link[], Node[]] {
		let nodes: Node[] = [];
		let links: Link[] = [];

		for (const n of data.nodes) {
			nodes.push({ id: n, group: 1 });
		}
		for (const e of data.edges) {
			const [source, target, value] = e;
			if (value > 0.1) {
				links.push({ source, target, value, weight: value });
			}
		}

		let results = jLouvain().nodes(data.nodes).edges(links)();
		for (const n of nodes) {
			n["group"] = results[n.id];
		}

		return [links, nodes];
	}
</script>

<Header />
<main>
	{#if links.length > 0 && nodes.length > 0}
		<Graph width={1000} height={800} {links} {nodes} />
	{/if}
</main>

<style>
</style>
