const STATUS_INITIAL = 0;
const STATUS_LOADING = 1;

export default {
  data(){
    return {
      currentStatus: 0
    }
  },
  computed: {
    isInitial(){
      return this.currentStatus === STATUS_INITIAL;
    },
    isLoading(){
      return this.currentStatus === STATUS_LOADING;
    }
  },
  methods: {
    validateForm(){
      this.currentStatus = STATUS_LOADING;
      const values = Object.values(this.creds);
      for(let i = 0; i < Object.keys(this.creds).length; i++){
        if(!values[i].length){
          return false;
        }
      }
      return true;
    }
  }
}