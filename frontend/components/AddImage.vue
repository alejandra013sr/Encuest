<template>
  <div class="add-image">
    <img class="add-image__placeholder" v-if="image" :src="image">
    <div class="add-image__icon" v-if="isInitial">
      <font-awesome-icon icon="image"/>
    </div>
    <input 
      class="input-file" 
      type="file" 
      accept="image/*" 
      @change="fileChange($event.target.files)"
      v-if="isInitial"
    >
    <span v-if="isSuccess">Imagen guardada correctamente</span>
    <span v-if="isFailed">Error al guardar la imagen</span>
    <Loader v-if="isSaving" />
  </div>
</template>
<script>

const STATUS_INITIAL = 0;
const STATUS_LOADED = 1;
const STATUS_SAVING = 2;
const STATUS_SUCCESS = 3;
const STATUS_FAILED = 4;

export default {
  name: 'AddImage',
  data(){
    return {
      image: null,
      uploadedFiles: [],
      uploadError: null,
      currentStatus: null
    }
  },
  computed: {
    isInitial(){
      return this.currentStatus === STATUS_INITIAL;
    },
    isLoaded(){
      return this.currentStatus === STATUS_LOADED;
    },
    isSaving(){
      return this.currentStatus === STATUS_SAVING;
    },
    isSuccess(){
      return this.currentStatus === STATUS_SUCCESS;
    },
    isFailed(){
      return this.currentStatus === STATUS_FAILED;
    },
    user(){
      return this.$store.getters.loggedUser;
    }
  },
  methods: {
    reset(){
      this.currentStatus = 0;
    },
    async fileChange(fileList){
      
      if(!fileList.length) return;

      const file = fileList[0];

      const fileBase64 = await this.toBase64(file);

      console.log(file);
      console.log(fileBase64);

      this.image = fileBase64;


      this.save(fileBase64);
    },
    toBase64(file){
      return new Promise((resolve, reject) => {

        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
          this.currentStatus = STATUS_LOADED;
          resolve(reader.result);
        };
        reader.onerror = error => reject(error);

      })
    },
    async save(file){
      console.log(this.$axios);
      this.currentStatus = STATUS_SAVING;
      try {
        const res = await this.$axios.post('/imagenes/image/', {
          title: 'Titulo',
          description: 'Description',
          email: this.user.email,
          image: file
        });
        this.currentStatus = STATUS_SUCCESS;
        console.log(res)
      } catch (error){
        this.currentStatus = STATUS_FAILED;
        console.log(error);
      };
    }
  },
  mounted(){
    this.reset();
  }
}

</script>