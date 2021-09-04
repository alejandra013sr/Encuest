export default async function ({ $auth, $axios }) {

  if(process.server){
    console.log('En el server');
    try {
      const res = await $axios({
                url: '/login',
                baseUrl: 'http://backend:8000'
              });
      console.log(res);
      console.log($axios);

    } catch (e) {
      console.log(e.toJSON());
    }
  }
}