<template>
	<div class="input">
		<input type="password" :name="name" :placeholder="placeholder" v-model="pass">
	</div>
</template>
<script>
export default {
	name: 'InputPassword',
	data(){
		return {
			pass: ''
		}
	},
	props: {
		name: String,
		placeholder: String
	}
}

</script>