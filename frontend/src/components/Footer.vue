<template>
  <div class="footer__block">
      <div class="footer">
          
          <div class="footer_service__title" align="left">
            <h4 style="border-bottom: 1px solid red">
                АВТОСЕРВИС "АМБЕРГ"
            </h4>
            <p>
                Станция технического обслуживания легковых автомобилей. 
                Мы оказываем полный спектр услуг по ремонту автомобилей практически всех марок, произведенных отечественными и зарубежными компаниями.
            </p>      
          </div>
          <div class="connection" align="left">
              <h5 style="border-bottom: 1px solid red; margin-bottom: 15px;">
                  СВЯЗЬ С НАМИ
              </h5>
              <p class="connect_item">
                  Позвоните нам!
              </p>
              <p class="connect_item">
                  Напишите нам!
              </p>
          </div>
          <div class="footer_nav" align="left">
              <h5 style="margin-left: 30px; border-bottom: 1px solid red; margin-bottom: 15px;">МЕНЮ</h5>
              <ul class="nav-bar-items">
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">ГЛАВНАЯ</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">РЕМОНТ</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">УСЛУГИ</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">АВТОЭЛЕКТРИКА</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">МАГАЗИН</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">О КОМПАНИИ</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">КОНТАКТЫ</a>
                </li>
                <li class="navitem">
                <a class="navlink" aria-current="page" href="#">ФИЛИАЛ</a>
                </li>
            </ul>
          </div>
        
        <div class="contacts" align="left">
            <h5 style="border-bottom: 1px solid red; margin-bottom: 15px;">КОНТАКТЫ</h5>
            <p>г. Витебск,ул.Воинов-Интернационалистов 1В</p>
            <p>Городcкой: 8 (0212) 25-20-83</p>
            <p>МТС: +375 29 719-34-40, +375 29 513-96-96</p>
            <p>A1: +375 29 693-73-42, +375 29 613-96-96</p>
            <p>kolya_005@mail.ru</p>
        </div>
      </div>
    
      
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.footer__block{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    color: #f3f3f3;
    position: absolute;
    bottom: 30px;
    top: 3300px;
    height: 300px;
    
}

.footer{
    border: 1px solid gray;
    width: 1920px;
    display: flex;
    align-content: center;
    justify-content: center;
    /* justify-content: space-around; */
    gap: 50px;
    background: rgb(0, 0, 0);
    padding: 30px;
    flex-direction: row;
}
.footer_service__title{
    display: flex;
    flex-direction: column;
    width: 200px;

}
.nav-bar-items{
    list-style-type: none;
    font-size: 16px;
}
.navitem{
    margin-bottom: 5px;
    border-bottom: 1px solid black;
    
}
.navlink{
    text-decoration: none;
    color: #afafaf;
}

p{
    color: #afafaf;
}

.contacts{
    width: 500px;
}

.connect_item{
    border-bottom: 1px solid black;
    margin-bottom: 5px;
}
</style>