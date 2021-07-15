<template>
	<div class="input">
		<input 
			type="text" 
			:name="name" 
			:placeholder="placeholder"
			:value="value"
			@input="$emit('input', $event.target.value)"
		>
	</div>
</template>
<script>
export default {
	name: 'InputText',
	props: {
		name: String,
		placeholder: String,
		value: String
	}
}

</script>