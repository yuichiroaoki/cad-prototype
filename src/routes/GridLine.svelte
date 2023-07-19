<script lang="ts">
	import { onMount } from 'svelte';
	import * as THREE from 'three';
	import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

	let container: HTMLDivElement;

	onMount(() => {
		// Scene
		const scene = new THREE.Scene();

		// Camera
		const camera = new THREE.PerspectiveCamera(75, 1000 / 1000, 0.1, 1000);
		//   const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
		camera.position.z = 5;

		// Renderer
		const renderer = new THREE.WebGLRenderer();
		renderer.setSize(1000, 1000);
		//   renderer.setSize(window.innerWidth, window.innerHeight);
		container.appendChild(renderer.domElement);
		const controls = new OrbitControls(camera, renderer.domElement);

		// Grid
		const size = 10;
		const divisions = 10;
		const gridHelper = new THREE.GridHelper(size, divisions);
		scene.add(gridHelper);

		gridHelper.rotation.x += 0.5;
		gridHelper.rotation.y += 0.1;

		function animate() {
			requestAnimationFrame(animate);

			// required if controls.enableDamping or controls.autoRotate are set to true
			controls.update();

			renderer.render(scene, camera);
		}

		animate();

		// Clean up the Three.js scene on component unmount
		return () => {
			renderer.dispose();
			scene.remove(gridHelper);
		};
	});
</script>

<div bind:this={container} />
