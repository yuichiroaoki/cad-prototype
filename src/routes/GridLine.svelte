<script lang="ts">
	import { onMount } from 'svelte';
	import * as THREE from 'three';
	import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
	import { STLLoader } from 'three/addons/loaders/STLLoader.js';

	let container: HTMLDivElement;

	onMount(() => {
		// Scene
		const scene = new THREE.Scene();
		scene.background = new THREE.Color(0x999999);

		// Camera
		const camera = new THREE.PerspectiveCamera(35, 1000 / 1000, 1, 500);
		const cameraTarget = new THREE.Vector3(0, -0.25, 0);

		camera.position.set(0, 0, 5);

		// Grid
		const size = 50;
		const divisions = 50;
		const gridHelper = new THREE.GridHelper(size, divisions, 0xffffff, 0x555555);
		gridHelper.position.y = -0.5;

		scene.add(gridHelper);
		gridHelper.receiveShadow = true;

		// Renderer
		const renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setSize(1000, 1000);
		renderer.useLegacyLights = false;

		container.appendChild(renderer.domElement);

		const loader = new STLLoader();
		loader.load('src/lib/images/slotted_disk.stl', function (geometry: any) {
			const material = new THREE.MeshPhongMaterial({
				color: 0xff9c7c,
				specular: 0x494949,
				shininess: 200
			});
			const mesh = new THREE.Mesh(geometry, material);
			mesh.position.set(0, -0.25, 0.6);
			mesh.rotation.set(0, -Math.PI / 2, 0);
			mesh.scale.set(0.5, 0.5, 0.5);

			mesh.castShadow = true;
			mesh.receiveShadow = true;

			scene.add(mesh);

			render();
		});

		// Lights
		scene.add(new THREE.HemisphereLight(0x8d7c7c, 0x494966, 3));

		const controls = new OrbitControls(camera, renderer.domElement);
		controls.addEventListener('change', render);
		controls.target.set(0, 0, 2);
		controls.update();

		function render() {
			camera.lookAt(cameraTarget);

			renderer.render(scene, camera);
		}

		// Clean up the Three.js scene on component unmount
		return () => {
			renderer.dispose();
			scene.remove(gridHelper);
		};
	});
</script>

<div bind:this={container} />
