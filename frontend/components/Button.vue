<template>
	<button class="button" @click="$emit('click', $event)">
		<slot></slot>
	</button>
</template>
<script>

export default {
	name: 'Button'
}

</script>