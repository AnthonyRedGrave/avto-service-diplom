<template>
  <div class="repairtype_block">
      {{serviceData}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ServiceType',
    data(){
        return {
            serviceData:{}
        }
    },
    created() {
        this.getServiceData()
    },
    methods:{
        getServiceData(){
            axios.get(
                `http://localhost:8000/api/services/${this.$route.query.id}`
            ).then((response) =>{
                this.serviceData = response.data
            }).catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>