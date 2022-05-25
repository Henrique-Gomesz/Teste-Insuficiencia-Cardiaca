import random
import string
import cherrypy
import sqlite3
import json
import os

from func import calculo
class site_coracao(object):
    @cherrypy.expose
    def index(self):
        return """
       
        
              
        <!doctype html>
        <html lang="pt-br">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
            <!--CSS-->
            <link rel="stylesheet" href="style.css">
            <title>Teste coração</title>  
            <style>
            
              .btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:visited {
    background-color:#ffbfbf !important;
}
             .carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
}

.carousel-control-next-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
}
              </style>
          </head>
          <body style="background-color: #ffbfbf;">
            <br>
            <header>
              <div class="container d-flex justify-content-center"  style="padding-top: 50px;">
                <h1 class="display-4">TESTE DE INSUFICIÊNCIA CARDÍACA</h1>
              </div>
            </header>
            <form method="post" action="exibe" style="padding-top: 70px;">
              <section>
                  <div class="container">
                    <div id="carouselExampleIndicators" class="shadow p-3 mb-5 bg-white rounded carousel slide" style="border-radius:20px; box-shadow: 10,10,10; background-color: #ffffff" >
                      <br>
                      <div class="carousel-inner" >
                        <div class="carousel-item active">
                          <div class="d-flex justify-content-center">
                              
                                <h3 style="font-size: 35px;" class="display-4">Digite sua idade</h3>
                              </div>
                              <br>
                                <div class="d-flex justify-content-center ">
                                    <input type="number" class="form-control" style="width: 500px;" placeholder="Digite aqui" name="idade" required>
                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center" >
                                                  <h3 style="font-size: 35px;" class="display-4">Qual seu sexo?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                                  <select class="custom-select" style="width: 500px;" name="sexo" required>
                                <option selected>Selecione seu sexo</option>
                                <option value="F">Feminino</option>
                                <option value="M">Masculino</option>
                                                  </select>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Tipo de dor no peito?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                                  <select class="custom-select" style="width: 500px;" name="tipo_dor_peito" required>
                                <option selected>Selecione seu tipo de dor</option>
                                <option value="TA">TA</option>
                                <option value="ATA">ATA</option>
                                <option value="NAP">NAP</option>
                                <option value="ASY">ASY</option>
                                                  </select>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Qual sua pressão arterial em repouso?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                <input type="number" class="form-control" style="width: 500px;" placeholder="Digite aqui" name="pressao_arterial" required>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Qual seu nível de colesterol?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                <input type="number" class="form-control" style="width: 500px;" placeholder="Digite aqui" name="colesterol" required>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Qual seu nível de glicemia?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                <input type="number" class="form-control" style="width: 500px;" placeholder="Digite aqui" name="glicemia" required>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Qual é o resultado de seu eletrocardiograma?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                                  <select class="custom-select" style="width: 500px;" name="eletrocardiograma" required>
                                <option selected>Selecione o resultado</option>
                                <option value="Normal">Normal</option>
                                <option value="ST">ST</option>
                                <option value="LVH">LVH</option>
                                                  </select>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Qual sua frequencia cardiaca máxima?</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
              
                                <div class="form-group">
                                  <input type="number" min="60" max="202" class="form-control" name="frequencia_cardiaca" style="width: 500px;" placeholder="Digite aqui" required>
                                </div>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Angina induzida por exercicio</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                                  <select class="custom-select" style="width: 500px;" name="angina" required>
                                <option selected>Selecione uma opção</option>
                                <option value="Y">Sim</option>
                                <option value="N">Não</option>
                                                  </select>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">Pico antigo</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                <input type="text" class="form-control" style="width: 500px;" name="pico_antigo" placeholder="Digite aqui" required>
                                                </div>
                                              </div>
                                              <div class="carousel-item">
                                                <div class="d-flex justify-content-center">
                                                  <h3 style="font-size: 35px;" class="display-4">ST_Slope</h3>
                                                </div>
                                                <br>
                                                <div class="d-flex justify-content-center ">
                                                  <select class="custom-select" style="width: 500px;" name="st_slope" required>
                                <option selected>Selecione uma opção</option>
                                <option value="Up">Subindo</option>
                                <option value="Flat">Plano</option>
                                <option value="Down">Descendo</option>
                                                  </select>
                                                </div>
                                              </div>
                                            </div>
                                            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                              <span  class="carousel-control-prev-icon" aria-hidden="true"></span>
                                              <span class="sr-only">Previous</span>
                                            </a>
                                            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                              <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                              <span class="sr-only">Next</span>
                                            </a>
                                            <br>
                                            <br>
                                            <div class="container d-flex justify-content-center ">
                                              <input class=" btn-primary justify-content-center btn btn-lg btn-outline-light " type="submit">
                                            </div>
                                            <br>
                                            <br>
                                            <ol class="carousel-indicators">
                                              <li style="background-color: #ffbfbf;" data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                              <li style="background-color: #ffbfbf;"  data-target = "#carouselExampleIndicators" data-slide-to="1"></li>
                                              <li style="background-color: #ffbfbf;" data-target= "#carouselExampleIndicators" data-slide-to="2"></li>
                                              <li style="background-color: #ffbfbf; "data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                                              <li style="background-color: #ffbfbf; "data-target="#carouselExampleIndicators" data-slide-to="4"></li>
                                              <li style="background-color: #ffbfbf;" data-target="#carouselExampleIndicators" data-slide-to="5"></li>
                                              <li style="background-color: #ffbfbf;" data-target="#carouselExampleIndicators" data-slide-to="6"></li>
                                              <li style="background-color: #ffbfbf;" data-target="#carouselExampleIndicators" data-slide-to="7"></li>
                                              <li style="background-color: #ffbfbf;" data-target="#carouselExampleIndicators" data-slide-to="8"></li>
                                              <li style="background-color: #ffbfbf; "data-target="#carouselExampleIndicators" data-slide-to="9"></li>
                                              <li style="background-color: #ffbfbf; "data-target="#carouselExampleIndicators" data-slide-to="10"></li>
                                            </ol>
                                            <br>
                                          </div>
                                        </div>
                                  
            </form>
            </section>
            <div class="container">
              <footer class="bg-light text-center text-lg-start">
    
                <div class="text-center p-3">
                  © 2022 Copyright <br>
                  <a target="_blank" class="text-dark" href="https://github.com/Henrique-Gomesz">Henrique Gomes Junqueira</a> |
                  <a class="text-dark"href="">Leonardo Gomes Anholetto</a>
                </div>
               
              </footer>
            </div>
            <!-- Optional JavaScript; choose one of the two! -->
            <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
        
          </body>
        </html>
        


        """
    def calculo(idade,sexo,tipo_dor_peito,pressao_arterial,colesterol,glicemia,eletrocardiograma,frequencia_cardiaca,angina,pico_antigo,st_slope):
      idade=int(idade)
      pressao_arterial=int(pressao_arterial)
      colesterol=int(colesterol)
      glicemia=int(glicemia)
      frequencia_cardiaca=int(frequencia_cardiaca)
      pico_antigo=float(pico_antigo)
      if st_slope=='DOWN':
          if tipo_dor_peito=='ASY':
              if eletrocardiograma<=126:
                  if idade<=62:
                      if frequencia_cardiaca<=140:
                          return 1
                      else:
                          return 1
                  else:
                      return 0
              else:
                  return 1
          elif tipo_dor_peito=='ATA':
              return 0
          elif tipo_dor_peito=='NAP':
              if colesterol<=113:
                  return 1
              else:
                  return 0
          else:
              return 0
      elif st_slope=='FLAT':
          if tipo_dor_peito=='ASY':
              if sexo=='F':
                  if colesterol<=341:
                      if idade<=52:
                          if idade<=38:
                              return 1
                          else:
                              if frequencia_cardiaca<=108:
                                      return 1
                              else:
                                  if colesterol<=265:
                                      return 0
                                  else:
                                      return 1
                      else:
                          if idade<=63:
                              return 1 
                          else:
                              if pressao_arterial<=130:
                                  return 0
                              else:
                                  return 1
                  else: 
                      return 0
              else:
                  return 1
          elif tipo_dor_peito=='ATA':
              if eletrocardiograma=='LVH':
                  if colesterol<=236:
                      return 0
                  else:
                      return 0
              elif eletrocardiograma=='NORMAL':
                  if idade<=36:
                      return 1
                  else:
                      if colesterol<=0:
                          return 1
                      else:
                          if colesterol<=273:
                              return 0
                          else:
                              return 1
              else:
                  return 1     
          elif tipo_dor_peito=='NAP':
              if idade<=44:
                  return 0
              else:
                  if eletrocardiograma=='LVH':
                      if pressao_arterial<=125:
                          if frequencia_cardiaca<=160:
                              return 0
                          else:
                              return 0
                      else:
                          if idade <=63:  
                              return 1
                          else:  
                              return 0
                  elif eletrocardiograma=='NORMAL':
                      if pressao_arterial<=130:
                          if idade<=59:
                              if colesterol<=218:
                                  if pico_antigo<=0:
                                      return 1
                                  else:
                                      return 1
                              else:
                                  return 0
                          else:
                              return 1
                      else:
                          return 1 
                  else:
                      if colesterol<=0:
                          if frequencia_cardiaca<=119:
                              return 1
                          else:
                              return 0
                      else:
                          return 1
          else:
              if eletrocardiograma=='LVH':
                  if colesterol<=0:
                      return 1
                  else:
                      if idade<=56:
                          return 0
                      else:
                          return 0
              elif eletrocardiograma=='NORMAL':
                  if sexo=='M':
                      return 1
                  else:
                      return 0
              else:
                  return 1
      else:
          if tipo_dor_peito=='ASY':
              if pico_antigo<=0.4:
                  if colesterol<=0:
                      return 1
                  else:
                      if eletrocardiograma=='LVH':
                          if idade<=44:
                              return 1 
                          else:
                              if pressao_arterial<=115:
                                  return 0
                              else:
                                  if pressao_arterial<=130:
                                      return 1
                                  else:
                                      return 0 
                      if eletrocardiograma=='NORMAL':
                          if frequencia_cardiaca<=150:
                              return 0 
                          else:
                              if frequencia_cardiaca<=162:
                                  return 1 
                              else:
                                  if idade<=40:
                                      return 0
                                  else:
                                      return 0
                      if eletrocardiograma=='ST':
                          return 0
              else:
                  if frequencia_cardiaca<=166:
                      if frequencia_cardiaca<=96:
                          return 0
                      else:
                          if idade<=59:
                              return 1
                          else:
                              if colesterol<=0:
                                  return 0
                              else:
                                  return 1
                  else: 
                      return 0
          elif tipo_dor_peito=='ATA':
              return 0
          elif tipo_dor_peito=='NAP':
              if pico_antigo<=1.9:
                  return 0 
              else:
                  return 1
          else:
              if colesterol<=240:
                  if pressao_arterial<=134:
                      if eletrocardiograma=='LVH':
                          return 0
                      else:
                          return 1
                  else:
                      return 0
              else:
                  return 1
    @cherrypy.expose
    def exibe(self,idade,sexo,tipo_dor_peito,pressao_arterial,colesterol,glicemia,eletrocardiograma,frequencia_cardiaca,angina,pico_antigo,st_slope):
      resp=calculo(idade,sexo,tipo_dor_peito,pressao_arterial,colesterol,glicemia,eletrocardiograma,frequencia_cardiaca,angina,pico_antigo,st_slope)
      if resp == 1:
        return """
              
                      <!doctype html>
                      <html lang="pt-br">
                        <head>
                          <!-- Required meta tags -->
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      
                          <!-- Bootstrap CSS -->
                          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
                          <!--CSS-->
                          <link rel="stylesheet" href="style.css">
                          <title>RESULTADO DO TESTE</title>  
                          <style>
                          
                            .btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:visited {
                  background-color:#ffbfbf !important;
              }
                          .carousel-control-prev-icon {
                  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
              }

              .carousel-control-next-icon {
                  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
              }
                            </style>
                        </head>
                        <body style="background-color: #ffbfbf;">
                          <br>
                          <header>
                            <div class="container d-flex justify-content-center"  style="padding-top: 50px;">
                              <h1 class="display-4">RESULTADO</h1>
                            </div>
                          </header>
                        <section>
                            <div class="container">
                                      <div style="background-color: #ffffff;">
                                          <div class="d-flex justify-content-center">
                                              Seu resultado foi positivo para insuficiência cardíaca.<br>
                                          </div>
                                              <div class="d-flex justify-content-center">
                                                  <a style="color: #ff8080;"  target="_blank" href="https://www.google.com/search?q=cardiologista+perto+de+mim">Procure o médico mais próximo de você!</a>
                                              </div>
                                      </div>
                                    
                            </div>
                        </section>
                      
                          <div class="container" style="padding-top: 50px;">
                            <footer class="bg-light text-center text-lg-start">
                  
                              <div class="text-center p-3">
                                © 2022 Copyright <br>
                                <a target="_blank" class="text-dark" href="https://github.com/Henrique-Gomesz">Henrique Gomes Junqueira</a> |
                                <a class="text-dark"href="">Leonardo Gomes Anholetto</a>
                              </div>
                            
                            </footer>
                          </div>
                          <!-- Optional JavaScript; choose one of the two! -->
                          <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
                          <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                          <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
                      
                        </body>
                      </html>
                      

        """
      else:
        return """
                
        <!doctype html>
        <html lang="pt-br">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
            <!--CSS-->
            <link rel="stylesheet" href="style.css">
            <title>RESULTADO DO TESTE</title>  
            <style>
            
              .btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:visited {
    background-color:#ffbfbf !important;
}
             .carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
}

.carousel-control-next-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff8080' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
}
              </style>
          </head>
          <body style="background-color: #ffbfbf;">
            <br>
            <header>
              <div class="container d-flex justify-content-center"  style="padding-top: 50px;">
                <h1 class="display-4">RESULTADO</h1>
              </div>
            </header>
           <section>
               <div class="container">
                        <div style="background-color: #ffffff;">
                            <div class="d-flex justify-content-center">
                                Seu resultado foi negativo para insuficiência cardíaca.<br>
                            </div>
                                <div class="d-flex justify-content-center">
                                    <a style="color: #ff8080;"  target="_blank" href="https://kozma.com.br/10-dicas-para-cuidar-bem-da-saude-do-seu-coracao/">Dicas de como cuidar do coração</a>
                                </div>
                        </div>
                       
               </div>
           </section>
        
            <div class="container" style="padding-top: 50px;">
              <footer class="bg-light text-center text-lg-start">
    
                <div class="text-center p-3">
                  © 2022 Copyright <br>
                  <a target="_blank" class="text-dark" href="https://github.com/Henrique-Gomesz">Henrique Gomes Junqueira</a> |
                  <a class="text-dark"href="">Leonardo Gomes Anholetto</a>
                </div>
               
              </footer>
            </div>
            <!-- Optional JavaScript; choose one of the two! -->
            <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
        
          </body>
        </html>
        
        
        """


        




	

if __name__ == "__main__":
    conf = {
        '/': {
            'tools.staticdir.root': os.getcwd()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    cherrypy.quickstart(site_coracao(), '/', conf)