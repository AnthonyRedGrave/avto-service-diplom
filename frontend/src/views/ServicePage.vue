<template>
  <div class="servicetype_block">
      <div class="servicetype_title">
          <h1>{{serviceData.title}}</h1>
      </div>
      <div class="servicetype_contacts_block">
        <div class="servicetype_contact" v-for="contact in serviceData.contacts" :key="contact.id">
            <h3>{{contact.phone}} {{contact.first_name}} {{contact.last_name}}</h3>
            {{contact.working_mode}}
        </div>
      </div>
      <div class="servicetype_work_info_block">
          <div class="work_info_time">
            <h3>Время проведения услуги:</h3>
            <h2>{{serviceData.time}}</h2>
          </div>
          <div class="work_info_price">
            <h3>Стоимость услуги:</h3>
            <h2>{{serviceData.price}}</h2>
          </div>
          <div class="work_info_warranty">
            <h3>Гарантия:</h3>
            <h2>{{serviceData.warranty}}</h2>
          </div>

      </div>
        <hr>
      <div class="servicetype_body">
          <div class="servicetype_text" v-html="serviceData.text" align="left">
          </div>
          
          <div class="servicetype_suggestions">
              <h3>Сотрудниками нашего СТО выполняются следующие работы:</h3>
              <ul>
                <li v-for="sugg in serviceData.suggestions" :key="sugg">{{sugg}}</li>
              </ul>
          </div>
      </div>
      <OtherServices/>
  </div>
</template>

<script>
import OtherServices from '../components/OtherServices.vue'
import axios from 'axios'
export default {
    name: 'ServiceType',
    components:{
        OtherServices
    },
    data(){
        return {
            serviceData:{},
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
                console.log(this.serviceData)
            }).catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style>
.servicetype_block{
    position: static;

}
.servicetype_body{
    position: absolute;
    display: flex;
}

.servicetype_text{
    position: relative;
    width: 600px;
    left: 300px;
}

.servicetype_suggestions{
    position: relative;
    width: 600px;
    left: 400px;
}

.servicetype_contacts_block{
    border: 2px solid rgb(255, 93, 93);
    width: 600px;
    margin: 0 auto;
    padding: 10px;
    padding-bottom: 30px;
    border-radius: 13px;
    box-shadow: 5px 5px 5px black;
    margin-bottom: 35px;
}

.servicetype_work_info_block{
    display: flex;
    border: 2px solid rgb(155, 0, 0);
    padding: 10px;
    border-radius: 13px;
    margin: 0 auto;
    box-shadow: 5px 5px 5px black;
    margin-bottom: 55px;
    
    width: 600px;
    gap: 50px;
}

.work_info_time{
    width: 200px;
}
.work_info_price{
    width: 200px;
}
.work_info_warranty{
    width: 200px;
}

</style>