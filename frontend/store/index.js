import axios from 'axios'

export const state = () => ({
  counter: 0,
  images: []
})

export const mutations = {
  addImages(state, images){
    state.images = images;
  },
  deleteImage(state, index){
    console.log(state.images);
    state.images.splice(index, 1);
    console.log(state.images);
  },
  increment(state) {
    state.counter++
  }
}

export const getters = {
  isAuthenticated(state){
    return state.auth.loggedIn
  },
  loggedUser(state){
    return state.auth.user
  }
} 

export const actions = {
  async images({ commit }){
    const res = await this.$axios.get('/imagenes/image/');
    commit('addImages', res.data);
  },
  async deleteImage({ commit, dispatch, state }, id){
    const res = await this.$axios.$delete('/imagenes/image/', { data: { id } });
    const deleted = state.images.findIndex(image => image.id === id);
    if(deleted >= 0){
      commit('deleteImage', deleted);
    }

  }
}