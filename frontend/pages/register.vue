<template>
	<div class="login">
		<main class="login__main">
			<div class="login__title">
				<span>Resgistrate</span>
				<span>para continuar</span>
			</div>
			<form class="login__form" @submit.prevent>
				<InputText v-model="creds.name" name="name" placeholder="Nombre" />
				<InputEmail v-model="creds.email" name="email" placeholder="Correo" />
				<InputPassword v-model="creds.pass" name="password" placeholder="Contraseña" />
				<Button class="button--backgroundGradient" @click="register">Resgistrarme</Button>
			</form>	
			<div class="login__links">
				<Button class="button--borderGradient">Google</Button>
				<Button class="button--borderGradient">Facebook</Button>
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

import authMixin from '~/mixins/auth.mixin'
import { STATUS_INITIAL, STATUS_LOADING } from '~/utils/statusConstants' 
	
export default {
	layout: 'home',
	name: 'Register',
	mixins: [authMixin],
	// middleware: 'guest',
	data(){
		return {
			creds: {
				name: '',
				email: '',
				pass: ''
			}
		}
	},
	methods: {
		async register(){

			const validation = this.validateForm();

			if(!validation){
				this.$notify({
					type: 'warnning',
					// title: 'Error',
					text: 'Debes llenar todos los campos.'
				});
				this.currentStatus = STATUS_INITIAL;
				return;
			}

			try {
				await this.$axios.$post('http://localhost:8000/profile/users/', {
					"name": this.creds.name,
					"email": this.creds.email,
					"password": this.creds.pass
				});
				
				await this.$auth.loginWith('local', {
					data: {
						email: this.creds.email,
						password: this.creds.pass
					}
				});

				this.$router.push('/dashboard');

			} catch (e) {

				this.currentStatus = STATUS_INITIAL;

				const error = e.toJSON();

				this.$notify({
					type: 'error',
					title: 'Error',
					text: error.message
				});

			}
		}
	}
}

</script>