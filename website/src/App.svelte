<script lang="ts">
	import { onMount } from "svelte";
	import "./app.css";
	import Header from "./components/Header.svelte";

	import * as myc from "@apple/mycelium";
	import "@apple/mycelium/dist/style.css";

	onMount(async () => {
		const d = await loadGraphData();
		console.log(d);
	});

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
<main>here yee</main>

<style>
</style>
