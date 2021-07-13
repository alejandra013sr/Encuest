<template>
	<div class="input">
		<input 
			type="email" 
			:name="name" 
			:placeholder="placeholder"
			:value="value"
			@input="$emit('input', $event.target.value)"
		>
	</div>
</template>
<script>
export default {
	name: 'InputEmail',
	props: {
		name: String,
		placeholder: String,
		value: String
	}
}

</script>