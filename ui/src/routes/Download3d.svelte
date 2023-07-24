<!-- Download 3D STL file button -->

<script lang="ts">
	import axios from 'axios';

	async function download3d() {
		const filename = 'profile_shape.stl';
		const blobUrl = 'http://127.0.0.1:8000/load/model/profile_shape';
		axios
			.get(blobUrl, { responseType: 'blob' })
			.then(function (response) {
				const blobUrl = URL.createObjectURL(response.data);
				const anchor = document.createElement('a');
				anchor.href = blobUrl;
				anchor.target = '_blank';
				anchor.download = filename;
				anchor.click();
				URL.revokeObjectURL(blobUrl);
			})
			.catch(function (error) {
				console.log(error);
			});
	}
</script>

<h2>Download 3D STL file</h2>
<button on:click={download3d}>Download</button>
