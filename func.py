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