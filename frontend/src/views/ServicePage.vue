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
      <div class="servicetype_images">
            <div v-if="haveImages" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img :src="'http://localhost:8000/media/'+serviceData.images[0]" height="500" class="d-block w-80" alt="...">
                </div>
                <div v-if="this.serviceData.images.length == 2" class="carousel-item">
                  <img :src="'http://localhost:8000/media/'+serviceData.images[1]" height="500" class="d-block w-80" alt="...">
                </div>
                <div v-if="this.serviceData.images.length == 3" class="carousel-item">
                  <img :src="'http://localhost:8000/media/'+serviceData.images[2]" height="500" class="d-block w-80" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        <hr>
      <div class="servicetype_body">
          <div class="servicetype_text" v-html="serviceData.text" align="left">
          </div>
          
          <div class="servicetype_suggestions" align="left">
              <h3>Сотрудниками нашего СТО выполняются следующие работы:</h3>
              <hr>
              <ul class="suggestions_list">
                <li class="sugg_li" v-for="sugg in serviceData.suggestions" :key="sugg">{{sugg}}</li>
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
            haveImages: false
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
                if (this.serviceData.images.length !== 0){
                  this.haveImages = true
                }
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

.servicetype_images{
  padding-left: 520px;
  margin: 0 auto;
  margin-bottom: 50px;
}

.suggestions_list{
  list-style-type: none;
}

.sugg_li{
  font-size: 22px;
  margin-bottom: 15px;
}

</style>