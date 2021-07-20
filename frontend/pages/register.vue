<template>
	<div class="login">
		<header class="login__header">
			<div class="login__logo">
				<Logo width="80px" background="horizontalGradient" />
			</div>
			<div class="login__title">
				<span>Resgistrate</span>
				<span>para continuar</span>
			</div>
		</header>
		<main class="login__main">
			<form class="login__form" @submit.prevent>
				<InputText v-model="name" name="name" placeholder="Nombre" />
				<InputEmail v-model="email" name="email" placeholder="Correo" />
				<InputPassword v-model="pass" name="password" placeholder="Contraseña" />
				<Button class="button--backgroundGradient" @click="register">Resgistrarme</Button>
			</form>	
			<div class="login__links">
				<Button class="button--borderGradient">Google</Button>
				<Button class="button--borderGradient">Facebook</Button>
				<div>{{email}}</div>
			</div>
		</main>
		<footer class="login__footer">
			<span>¿Ya tienes una cuenta?.</span>
			<b>
				<NuxtLink to="/login" href="#">Ingresar</NuxtLink>
			</b>
		</footer>

	</div>
</template>
<script>
	
export default {
	name: 'Register',
	data(){
		return {
			name: '',
			email: '',
			pass: ''
		}
	},
	methods: {
		async register(){
			const res = await this.$axios.$post('http://localhost:8000/profile/users/', {
				"name": this.name,
				"email": this.email,
				"password": this.pass
			});
			console.log(res);
		}
	}
}

</script>