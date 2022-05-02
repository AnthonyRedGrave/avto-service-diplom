<template>
  <div class="service_order_block">
      <br>
      <h2>ЗАКАЗ УСЛУГИ</h2>
      <br>
      <div v-if="order_made" class="made_order_title">
        <br>
        <div class="alert alert-success" role="alert">
            Спасибо! Ваш заказ принят и вам позвонят!
        </div>
        <br>
      </div>
      
      <form @submit.prevent>
          <div class="services_block">
            <div v-for="item in allItems" :key="item.id" class="service_block">
                <div class="service_image">
                    <img v-if="item.images.length == 0" width="150" class="image_service" src="~@/assets/avto-service-logo.jpeg" alt="">
                    <img v-else width="150" height="310" class="image_service" :src="'http://localhost:8000/media/'+item.images[0]" alt="">
                </div>
                <div class="service_title" style="font-size: 22px;">
                    {{item.title}}
                </div>
                <div class="service_price" style="font-size: 22px;">
                    
                    <button type="button" class="btn btn-outline-secondary">{{item.price}}</button>
                </div>
                <div class="order__button">
                    <button type="button" class="btn btn-outline-primary" @click="addOrder(item)">Заказать услугу</button>
                </div>
            </div>
          </div>
          <div v-if="total_price" class="order_total">
              <br>
              <h2>ИТОГ ВАШЕГО ЗАКАЗА</h2>
              <br>
              <div v-if="is_error" class="error_order_title">
                <div class="alert alert-danger" role="alert">
                    Заполните все поля!
                </div>
              </div>
              <div class="pre_ordered_total_price">
                  <h4>Цена: {{total_price}} б.р.</h4>
              </div>
              <br>
              <div class="pre_ordered_items" align="left">
                <div class="pre_ordered_item" v-for="pre_item in ordered_items" :key="pre_item.id"> 
                    <div class="pre_ordered_item__title">
                        {{pre_item.title}}
                    </div>
                </div>
              </div>
              <div class="user_credentials">
                  <label for="">Ваше имя</label>
                  <input v-model="firstname" type="text" class="form-control firstname_input">
                  <label for="">Ваша фамилия</label>
                  <input v-model="lastname" type="text" class="form-control lastname_input">
                  <label for="">Ваш телефон</label>
                  <input v-model="phone" type="text" class="form-control phone_input">
              </div>
              <div class="make_order_butt">
                  <br>
                  <button type="submit" class="btn btn-outline-primary" @click="createOrder()">Сделать заказ</button>
              </div>
          </div>
          <div v-else class="no_order_total">
              <br>
              <h2>Выберите услугу...</h2>
              <br>

              
          </div>
      </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ServiceOrder',
    data(){
        return{
            data:{},
            allItems:[],
            ordered_items: [],
            total_price: 0,
            order_made: false,
            firstname: '',
            lastname: '',
            phone: '',
            is_error: false
        }
    },
    created(){
        this.getAllItems()
    },
    methods: {
        getAllItems(){
            axios.get(
                'http://localhost:8000/api/services/',{
            }).then((response) =>{
                this.allItems = response.data

            }).catch((err)=>{
                console.log(err)
            })
        },
        addOrder(item){
            if (this.ordered_items.includes(item)){
                for( var i = 0; i < this.ordered_items.length; i++){ 
                    if ( this.ordered_items[i].id === item.id) { 
                        this.ordered_items.splice(i, 1);
                        this.total_price -= item.price_int
                    }
                }
            }
            else{
                this.ordered_items.push(item)
                this.total_price += item.price_int
            }
        

        },
        createOrder(){
            if (this.firstname == '' || this.lastname == '' || this.orders == [] || this.phone == ''){
                this.is_error = true
            }
            else{
                let order_id = []
                this.ordered_items.forEach(el =>{
                    order_id.push(el.id)
                })
                let data = {
                    first_name: this.firstname,
                    last_name: this.lastname,
                    orders: order_id,
                    phone: this.phone,
                }
                axios({
                        method: 'post',
                        url: 'http://localhost:8000/api/orders/make_order/',
                        data: data,
                        credentials: 'include',
                    }).then((responce) => {
                        console.log(responce.data)
                    })
                    .catch(err => {
                        console.log(err)
                    })

                console.log(data)
                this.order_made = true
                this.data = {}
                this.ordered_items = []
                this.total_price = 0
            }
            

        }
    },
    
}
</script>

<style>
.services_block{
    margin: 0 auto;
    width: 1000px;
}
.service_block{
    display: flex;
    border: 2px solid black;
    border-radius: 15px;
    margin-bottom: 15px;
    padding: 10px;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 30px;
}
.pre_ordered_items{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.user_credentials{
    display: flex;
    margin-top: 30px;
    margin-bottom: 30px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 30px;
}

.firstname_input{
    width: 500px;
}
.lastname_input, .phone_input{
    width: 500px;
}
</style>