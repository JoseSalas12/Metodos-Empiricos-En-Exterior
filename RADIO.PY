import tkinter 
from tkinter import Tk, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
from tkinter.constants import RIGHT
import math as ma


class Software:
    def __init__(self,Ventana):
        self.lb = 0
        self.wind = Ventana
        
        frame1 = tkinter.LabelFrame(self.wind)
        frame1.grid(row = 0 ,column = 0 ,sticky = 'WE')
        tkinter.Label(frame1,font=('Century Gothic',15),text = 'Metodos Empiricos En Exterior').pack()
        
        Pestañas = ttk.Notebook(self.wind,width="900", height="500")
        Pestañas.grid(row = 1 ,column = 0)
        
        pes1=ttk.Frame(Pestañas)
        pes2=ttk.Frame(Pestañas)
        pes3=ttk.Frame(Pestañas)
        pes4=ttk.Frame(Pestañas)
        pes5=ttk.Frame(Pestañas)

        Pestañas.add(pes1,text = 'OKUMURA-HATA')
        Pestañas.add(pes2,text = 'IKEGAMI')
        Pestañas.add(pes3,text = 'WALFISCH-BERTONI')
        Pestañas.add(pes4,text = 'WALFISCH-IKEGAMI')
        Pestañas.add(pes5,text = 'HATA COST 231')
        
        tkinter.Label(self.wind,font=('Century Gothic',10),text = 'Diseñado por: Jose Salas,Juan Cabas,Daniel Gomez,Martin Barros').place(x=0, y =600)
        tkinter.Label(self.wind,font=('Century Gothic',10),text = 'Docente:ING. Yesica Beltran').place(x=0, y =630)
        
        #OKAMURA-HATA
        frame2 = tkinter.LabelFrame(pes1,width=400,height=200)
        frame2.place(x = 100 , y = 250)
        tkinter.Label(frame2,font=('Century Gothic',15),text = 'RESULTADOS').place(x= 130, y =0)
        tkinter.Label(frame2,font=('Century Gothic',13),text = 'Las perdidas totales son:').place(x= 0, y =30)
        
        tkinter.Label(pes1,font=('Century Gothic',10),text ='Frecuencia(Mhz)').place(x=100 , y =25)
        self.Frecuencia = tkinter.Entry(pes1)
        self.Frecuencia.place(x= 215, y = 30)
        
        tkinter.Label(pes1,font=('Century Gothic',10),text ='Altura Transmisor(m)').place(x=80 , y =65)
        self.Htx = tkinter.Entry(pes1)
        self.Htx.place(x= 215, y = 70)

        tkinter.Label(pes1,font=('Century Gothic',10),text ='Altura Receptor(m)').place(x=85, y =105)
        self.Hrx = tkinter.Entry(pes1)
        self.Hrx.place(x =215 , y = 115 )
        
        tkinter.Label(pes1,font=('Century Gothic',10),text ='Distancia(km)').place(x=115 , y =150)
        self.Distancia = tkinter.Entry(pes1)
        self.Distancia.place(x= 215, y = 160)
        
        tkinter.Label(pes1,font=('Century Gothic',10),text ='Zona').place(x=400 , y =25)
        
        tkinter.Label(pes1,font=('Century Gothic',10),text ='Tamaño de ciudad').place(x=400 , y =65)
        
        self.Var = tkinter.StringVar(pes1)
        self.Var.set('Zona')
        Opciones = ['Selecciona','Urbana','Suburbana','Rural']
        self.Opcion = ttk.OptionMenu(pes1,self.Var, *Opciones)
        self.Opcion.config(width = 15)
        self.Opcion.place(x = 460, y = 25)
        
        self.Var2 = tkinter.StringVar(pes1)
        self.Var2.set('Ciudad')
        Opciones2 = ['Selecciona','Grande','Media-Pequeña']
        self.Opcion2 = ttk.OptionMenu(pes1,self.Var2, *Opciones2)
        self.Opcion2.config(width = 15)
        self.Opcion2.place(x = 535, y = 65)
        
        self.mensaje = Label(pes1,text = "", fg = "red",font = ('Century Gothic',15) )
        self.mensaje.pack(side = 'bottom')
        
        self.Resultado = Label(frame2,text = "",fg = "black",font = ('Century Gothic',10) )
        self.Resultado.place(x=0 , y = 50)
        
        #BOTONES
        tkinter.Button(pes1,text = "        Calcular        ",command = self.Calculos_Okumura_Hata).place(x = 215 , y = 195)
        
        #IKEGAMI
        frame3 = tkinter.LabelFrame(pes2,width=400,height=200)
        frame3.place(x = 100 , y = 250)
        tkinter.Label(frame3,font=('Century Gothic',15),text = 'RESULTADOS').place(x= 130, y =0)
        tkinter.Label(frame3,font=('Century Gothic',13),text = 'Las perdidas totales son:').place(x= 0, y =30)
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Frecuencia(Mhz)').place(x=100 , y =25)
        self.Frecuencia2 = tkinter.Entry(pes2)
        self.Frecuencia2.place(x= 215, y = 30)
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Altura Receptor(m)').place(x=85 , y =65)
        self.Hrx2 = tkinter.Entry(pes2)
        self.Hrx2.place(x= 215, y = 70)

        tkinter.Label(pes2,font=('Century Gothic',10),text ='Altura del edificio(m)').place(x=70, y =105)
        self.Hedificio = tkinter.Entry(pes2)
        self.Hedificio.place(x =215 , y = 115 )
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Distancia(km)').place(x=115 , y =150)
        self.Distancia2 = tkinter.Entry(pes2)
        self.Distancia2.place(x= 215, y = 160)
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Ancho de la calle(m)').place(x=400 , y =25)
        self.W = tkinter.Entry(pes2)
        self.W.place(x= 540, y = 30)
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Lr').place(x=520 , y =65)
        self.Lr = tkinter.Entry(pes2)
        self.Lr.place(x= 540, y = 70)
        
        tkinter.Label(pes2,font=('Century Gothic',10),text ='Angulo de Incidencia').place(x=390 , y =105)
        self.AnguloIn = tkinter.Entry(pes2)
        self.AnguloIn.place(x= 540, y = 115)
        
        self.mensaje2 = Label(pes2,text = "", fg = "red",font = ('Century Gothic',15) )
        self.mensaje2.pack(side = 'bottom')
        
        self.Resultado2 = Label(frame3,text = "",fg = "black",font = ('Century Gothic',10) )
        self.Resultado2.place(x=0 , y = 50)
        
        tkinter.Button(pes2,text = "        Calcular        ",command = self.Calculos_Ikegami).place(x = 215 , y = 195)
        
        #WALSFISCH-BERTONI
        
        frame4 = tkinter.LabelFrame(pes3,width=400,height=200)
        frame4.place(x = 100 , y = 250)
        tkinter.Label(frame4,font=('Century Gothic',15),text = 'RESULTADOS').place(x= 130, y =0)
        tkinter.Label(frame4,font=('Century Gothic',13),text = 'Las perdidas totales son:').place(x= 0, y =30)
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Frecuencia(Mhz)').place(x=100 , y =25)
        self.Frecuencia3 = tkinter.Entry(pes3)
        self.Frecuencia3.place(x= 215, y = 30)
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Altura Transmisor(m)').place(x=80 , y =65)
        self.Htx2 = tkinter.Entry(pes3)
        self.Htx2.place(x= 215, y = 70)
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Altura Antena Movil(m)').place(x=60, y =105)
        self.Ham = tkinter.Entry(pes3)
        self.Ham.place(x =215 , y = 115 )
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Altura Media de Edificios(m)').place(x=30 , y =150)
        self.Hme = tkinter.Entry(pes3)
        self.Hme.place(x= 215, y = 160)
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Separacion Entre Edificios(m)').place(x=350 , y =25)
        self.b = tkinter.Entry(pes3)
        self.b.place(x= 540, y = 30)
        
        tkinter.Label(pes3,font=('Century Gothic',10),text ='Distancia entre transmisor y receptor(Km)').place(x=345 , y =65)
        self.Distancia3 = tkinter.Entry(pes3)
        self.Distancia3.place(x= 615, y = 70)
        
        self.mensaje3 = Label(pes3,text = "", fg = "red",font = ('Century Gothic',15) )
        self.mensaje3.pack(side = 'bottom')
        
        self.Resultado3 = Label(frame4,text = "",fg = "black",font = ('Century Gothic',10) )
        self.Resultado3.place(x=0 , y = 50)
        
        tkinter.Button(pes3,text = "        Calcular        ",command = self.Calculos_Walfisch_Bertoni).place(x = 215 , y = 195)
        
        #WALSFISCH-IKEGAMI
        frame5 = tkinter.LabelFrame(pes4,width=400,height=200)
        frame5.place(x = 100 , y = 250)
        tkinter.Label(frame5,font=('Century Gothic',15),text = 'RESULTADOS').place(x= 130, y =0)
        tkinter.Label(frame5,font=('Century Gothic',13),text = 'Las perdidas totales son:').place(x= 0, y =30)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Frecuencia(Mhz)').place(x=100 , y =25)
        self.Frecuencia4 = tkinter.Entry(pes4)
        self.Frecuencia4.place(x= 215, y = 30)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Altura Transmisor(m)').place(x=80 , y =65)
        self.Htx3 = tkinter.Entry(pes4)
        self.Htx3.place(x= 215, y = 70)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Altura Antena Movil(m)').place(x=60, y =105)
        self.Ham2 = tkinter.Entry(pes4)
        self.Ham2.place(x =215 , y = 115 )
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Altura Media de Edificios(m)').place(x=30 , y =150)
        self.Hme2 = tkinter.Entry(pes4)
        self.Hme2.place(x= 215, y = 160)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Separacion Entre Edificios(m)').place(x=350 , y =25)
        self.b2 = tkinter.Entry(pes4)
        self.b2.place(x= 540, y = 30)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Distancia entre transmisor y receptor(Km)').place(x=345 , y =65)
        self.Distancia4 = tkinter.Entry(pes4)
        self.Distancia4.place(x= 615, y = 70)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Angulo de Incidencia').place(x=390 , y =105)
        self.AnguloIn2 = tkinter.Entry(pes4)
        self.AnguloIn2.place(x= 540, y = 115)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Ancho de la calle(m)').place(x=400 , y =150)
        self.W2 = tkinter.Entry(pes4)
        self.W2.place(x= 540, y = 160)
        
        self.Var3 = tkinter.StringVar(pes4)
        self.Var3.set('Visibilidad')
        Opciones3 = ['Selecciona','Visibilidad','Sin Visibilidad']
        self.Opcion3 = ttk.OptionMenu(pes4,self.Var3, *Opciones3)
        self.Opcion3.config(width = 15)
        self.Opcion3.place(x = 750, y = 105)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Vista').place(x=700 , y =105)
        
        self.Var4 = tkinter.StringVar(pes4)
        self.Var4.set('Ubicacion')
        Opciones4 = ['Selecciona','Ciudades medias y Suburbanas sin vegetacion','Metropolis']
        self.Opcion4 = ttk.OptionMenu(pes4,self.Var4, *Opciones4)
        self.Opcion4.config(width = 15)
        self.Opcion4.place(x = 750, y = 25)
        
        tkinter.Label(pes4,font=('Century Gothic',10),text ='Ubicacion').place(x=680 , y =25)
        
        self.mensaje4 = Label(pes4,text = "", fg = "red",font = ('Century Gothic',15) )
        self.mensaje4.pack(side = 'bottom')
        
        self.Resultado4 = Label(frame5,text = "",fg = "black",font = ('Century Gothic',10) )
        self.Resultado4.place(x=0 , y = 50)
        
        tkinter.Button(pes4,text = "        Calcular        ",command = self.Calculos_Walfisch_Ikegami).place(x = 215 , y = 195)
        
        #HATA- COST 231
        frame6 = tkinter.LabelFrame(pes5,width=400,height=200)
        frame6.place(x = 100 , y = 250)
        tkinter.Label(frame6,font=('Century Gothic',15),text = 'RESULTADOS').place(x= 130, y =0)
        tkinter.Label(frame6,font=('Century Gothic',13),text = 'Las perdidas totales son:').place(x= 0, y =30)
        
        tkinter.Label(pes5,font=('Century Gothic',10),text ='Frecuencia(Mhz)').place(x=100 , y =25)
        self.Frecuencia5 = tkinter.Entry(pes5)
        self.Frecuencia5.place(x= 215, y = 30)
        
        tkinter.Label(pes5,font=('Century Gothic',10),text ='Altura Transmisor(m)').place(x=80 , y =65)
        self.Htx4 = tkinter.Entry(pes5)
        self.Htx4.place(x= 215, y = 70)
        
        tkinter.Label(pes5,font=('Century Gothic',10),text ='Altura Antena Movil(m)').place(x=60, y =105)
        self.Ham3 = tkinter.Entry(pes5)
        self.Ham3.place(x =215 , y = 115 )
        
        tkinter.Label(pes5,font=('Century Gothic',10),text ='Distancia entre transmisor y receptor(Km)').place(x=345 , y =25)
        self.Distancia5 = tkinter.Entry(pes5)
        self.Distancia5.place(x= 615, y = 25)
        
        self.Var5 = tkinter.StringVar(pes5)
        self.Var5.set('Cm')
        Opciones5 = ['Selecciona','Ciudad Media','Grandes Metropolis']
        self.Opcion5 = ttk.OptionMenu(pes5,self.Var5, *Opciones5)
        self.Opcion5.config(width = 15)
        self.Opcion5.place(x =535 , y = 65)
        
        tkinter.Label(pes5,font=('Century Gothic',10),text ='Tamaño de Ciudad').place(x=400 , y =65)
        
        
        self.mensaje5 = Label(pes5,text = "", fg = "red",font = ('Century Gothic',15) )
        self.mensaje5.pack(side = 'bottom')
        
        self.Resultado5 = Label(frame6,text = "",fg = "black",font = ('Century Gothic',10) )
        self.Resultado5.place(x=0 , y = 50)
        
        tkinter.Button(pes5,text = "        Calcular        ",command = self.Calculos_Hata_Cost).place(x = 215 , y = 195)
        
            
        
    def Validacion(self):
        return len(self.Frecuencia.get())!= 0 and len(self.Htx.get())!= 0 and len(self.Hrx.get())!= 0 and len(self.Distancia.get())!= 0
                 
    def Calculos_Okumura_Hata(self):
             
        if self.Validacion():
            self.mensaje["text"]= "CALCULADO"
    
            if 150 <= float(self.Frecuencia.get())<= 1500 and 30<= float(self.Htx.get())<= 200 and 1<= float(self.Hrx.get())<= 10 and 1<= float(self.Distancia.get())<=20 :
                
                if self.Var2.get() == 'Media-Pequeña':
                    self.Ahm=(1.1*ma.log10(float(self.Frecuencia.get()))-0.7)*(float(self.Hrx.get()))-(1.56*ma.log10(float(self.Frecuencia.get()))-0.8)
                    self.lb = 69.55+26.16*(ma.log10(float(self.Frecuencia.get())))-13.82*(ma.log10(float(self.Htx.get())))-self.Ahm+(44.9-6.55*(ma.log10(float(self.Htx.get()))))*(ma.log10(float(self.Distancia.get())))
                elif self.Var2.get() == 'Grande':
                    if float(self.Frecuencia.get())<= 200:
                        self.Ahm = (8.29*ma.pow(ma.log10(1.54*float(self.Hrx.get())), 2))-1.1
                        self.lb = 69.55+26.16*(ma.log10(float(self.Frecuencia.get())))-13.82*(ma.log10(float(self.Htx.get())))-self.Ahm+(44.9-6.55*(ma.log10(float(self.Htx.get()))))*(ma.log10(float(self.Distancia.get())))
                    else:
                        self.Ahm = (3.2*ma.pow(ma.log10(11.75*float(self.Hrx.get())), 2))-4.97
                        self.lb = 69.55+26.16*(ma.log10(float(self.Frecuencia.get())))-13.82*(ma.log10(float(self.Htx.get())))-self.Ahm+(44.9-6.55*(ma.log10(float(self.Htx.get()))))*(ma.log10(float(self.Distancia.get())))
                else:
                    self.mensaje["text"]="¡ ERROR ! SELECCIONE EL TAMAÑO DE LA CIUDAD"
                    
                if self.lb != 0:      
                    if self.Var.get() == 'Suburbana':
                        self.Lbs = self.lb-2*ma.pow((ma.log10(float(self.Frecuencia.get())/28)),2)-5.4
                        self.Resultado["text"]= "Lbs = "+str(self.Lbs)
                    elif self.Var.get() == 'Rural':
                        self.Lbr = self.lb-4.78*(ma.pow(ma.log10(float(self.Frecuencia.get())),2))+(18.33*ma.log10(float(self.Frecuencia.get())))-40.94
                        self.Resultado["text"]= "Lbr = "+str(self.Lbr) 
                    elif self.Var.get() == 'Urbana':
                        self.Resultado["text"]= "Lb = "+str(self.lb)
                    else:
                        self.mensaje["text"]= "¡ ERROR ! SELECCIONE LA ZONA " 
                else:
                    self.mensaje["text"]="¡ ERROR ! SELECCIONE EL TAMAÑO DE LA CIUDAD"
            else:
                self.mensaje["text"]="¡ ERROR ! LOS DATOS INGRESADOS NO SON APTOS PARA EL METODO"
                          
                    
            
                
        else:
            self.mensaje["text"] = "¡ ERROR ! RELLENA LOS DATOS"
    
    def Validacion2(self):
        return len(self.Frecuencia2.get())!= 0 and len(self.Hrx2.get())!= 0 and len(self.Hedificio.get())!= 0 and len(self.Distancia2.get())!= 0 and len(self.W.get())!= 0 and len(self.Lr.get())!= 0  and len(self.AnguloIn.get())!= 0             
    
    def Calculos_Ikegami(self):
        if self.Validacion2():
            self.mensaje2["text"]= "CALCULADO"
            self.lb2 = 26.65+30*(ma.log10(float(self.Frecuencia2.get())))+20*(ma.log10(float(self.Distancia2.get())))-10*(ma.log10(1+(3/float(self.Lr.get()))))-10*(ma.log10(float(self.W.get())))+20*(ma.log10(float(self.Hedificio.get())-float(self.Hrx2.get())))+10*(ma.log10(ma.sin(float(self.AnguloIn.get()))))
            self.Resultado2["text"]= "Lb = "+str(self.lb2)
        else:
           self.mensaje2["text"]= "¡ ERROR ! RELLENA LOS DATOS"          
    
    def Validacion3(self):
        return len(self.Frecuencia3.get())!= 0 and len(self.Htx2.get())!= 0 and len(self.Ham.get())!= 0 and len(self.Hme.get())!= 0 and len(self.b.get())!= 0 and len(self.Distancia3.get())!= 0    
    
    def Calculos_Walfisch_Bertoni(self):
        if self.Validacion3():
            self.mensaje3["text"]= "CALCULADO"
            self.A = 5*(ma.log10(ma.pow((float(self.b.get())/2), 2)+ma.pow((float(self.Hme.get())-float(self.Ham.get())), 2)))-9*(ma.log10(float(self.b.get())))+20*(ma.log10(ma.atan((2*(float(self.Hme.get())-float(self.Ham.get())))/float(self.b.get()))*(180/ma.pi)))
            self.lb3 = 89.55+ self.A+21*(ma.log10(float(self.Frecuencia3.get()))) + 38*(ma.log10(float(self.Distancia3.get())))-18*(ma.log10(float(self.Htx2.get())))-18*(ma.log10(1-(ma.pow(float(self.b.get()), 2)/(17*float(self.Htx2.get())))))
            self.Resultado3["text"]= "Lb = "+str(self.lb3)
        else:
           self.mensaje3["text"]= "¡ ERROR ! RELLENA LOS DATOS"  
           
    def Validacion4(self):
        return len(self.Frecuencia4.get())!= 0 and len(self.Htx3.get())!= 0 and len(self.Hme2.get())!= 0 and len(self.Hme2.get())!= 0 and len(self.b2.get())!= 0 and len(self.Distancia4.get())!= 0 and len(self.AnguloIn2.get())!= 0  and len(self.W2.get())!= 0  
    
    def Calculos_Walfisch_Ikegami(self):
        if self.Validacion4():
            self.mensaje4["text"]= "CALCULADO"
            if 900 <= float(self.Frecuencia4.get())<= 1800 and 0.01 <= float(self.Distancia4.get()) <= 30 and float(self.Htx3.get()) > float(self.Hme2.get()):
                if self.Var3.get() == 'Visibilidad':
                    if float(self.Distancia4.get()) >= 0.02 :
                        self.lb4 = 42.6+26*(ma.log10(float(self.Distancia4.get())))+20*(ma.log10(float(self.Frecuencia4.get())))
                        self.Resultado4["text"] = "Lb = "+str(self.lb4)
                elif self.Var3.get() == 'Sin Visibilidad' :
                    self.DeltaH = float(self.Hme2.get()) - float(self.Ham2.get())
                    
                    if 0 <= float(self.AnguloIn2.get())<= 35:
                        self.Lori = -10+0.3571*(float(self.AnguloIn2.get()))
                    elif 35 <= float(self.AnguloIn2.get()) <= 55:
                        self.Lori = 2.5+0.075*(float(self.AnguloIn2.get())-35)
                    elif 55 <= float(self.AnguloIn2.get()) <= 90:
                        self.Lori = 4-0.114*(float(self.AnguloIn2.get())-55)
                    
                    self.DeltaB = float(self.Htx3.get())-float(self.Hme2.get())
                    
                    if self.DeltaB >= 0 :
                        self.Kd = 18
                        self.Ka = 54
                    elif self.DeltaB < 0 and float(self.Distancia4.get()) >= 0.5 :
                        self.Ka = 54-0.8*(self.DeltaB)
                    elif self.DeltaB < 0 and float(self.Distancia4.get()) < 0.5:
                        self.Ka = 54-1.6*(self.DeltaB)
                    
                    if self.DeltaB < 0:
                        self.Kd = 18-15*(self.DeltaB/float(self.Hme2.get()))
                        
                    if self.Var4.get() == 'Ciudades medias y Suburbanas sin vegetacion':
                        self.Kf =-4+0.7*((float(self.Frecuencia4.get())/925)-1)
                        self.Lbsh = -18*(ma.log10(1+self.DeltaB))
                        self.Lmsd = self.Lbsh+ self.Ka+self.Kd*(ma.log10(float(self.Distancia4.get())))+self.Kf*(ma.log10(float(self.Frecuencia4.get())))-9*(ma.log10(float(self.b2.get())))
                        self.Lrts = -16.9-10*(ma.log10(float(self.W2.get())))+10*(ma.log10(float(self.Frecuencia4.get())))+20*(ma.log10(self.DeltaH))+self.Lori
                        self.lo = 32.44 + 20*(ma.log10(float(self.Distancia4.get())))+20*(ma.log10(float(self.Frecuencia4.get())))
                        self.lb4 = self.lo + self.Lrts + self.Lmsd
                        self.Resultado4["text"]= "Lb = "+str(self.lb4)
                    elif self.Var4.get() == 'Metropolis':
                        self.Kf = -4+1.5*((float(self.Frecuencia4.get())/925)-1)
                        self.Lbsh = -18*(ma.log10(1+self.DeltaB))
                        self.Lmsd = self.Lbsh+ self.Ka+self.Kd*(ma.log10(float(self.Distancia4.get())))+self.Kf*(ma.log10(float(self.Frecuencia4.get())))-9*(ma.log10(float(self.b2.get())))
                        self.Lrts = -16.9-10*(ma.log10(float(self.W2.get())))+10*(ma.log10(float(self.Frecuencia4.get())))+20*(ma.log10(self.DeltaH))+self.Lori
                        self.lo = 32.44 + 20*(ma.log10(float(self.Distancia4.get())))+20*(ma.log10(float(self.Frecuencia4.get())))
                        self.lb4 = self.lo + self.Lrts + self.Lmsd
                        
                        self.Resultado4["text"]= "Lb = "+str(self.lb4)
                    else:
                        self.mensaje4["text"]= "¡ ERROR ! SELECCIONA UNA UBICACION" 
                else:
                    self.mensaje4["text"]= "¡ ERROR ! SELECCIONA UNA VISTA" 
            else:
                self.mensaje4["text"]="¡ ERROR ! LOS DATOS INGRESADOS NO SON APTOS PARA EL METODO"    
                       
        else:
            self.mensaje4["text"]= "¡ ERROR ! RELLENA LOS DATOS"
    def Validacion5(self):
            return len(self.Frecuencia5.get())!= 0 and len(self.Htx4.get())!= 0 and len(self.Ham3.get())!= 0 and len(self.Distancia5.get())!= 0 
     
    def Calculos_Hata_Cost (self):
        if self.Validacion5():
            self.mensaje5["text"] = "DATO GUARDADO"
            if 1500 <= float(self.Frecuencia5.get()) <= 2000 and 30 <= float(self.Htx4.get()) <= 200 and 1 <= float(self.Ham3.get()) <= 10 and 1 <= float(self.Distancia5.get()) <= 20 :
            
                if self.Var5.get() == 'Ciudad Media':
                    self.Cm = 0
                    self.Ahm2=(1.1*ma.log10(float(self.Frecuencia5.get()))-0.7)*(float(self.Ham3.get()))-(1.56*ma.log10(float(self.Frecuencia5.get()))-0.8)
                    self.lb5 = 46.3 + 33.9*(ma.log10(float(self.Frecuencia5.get())))-13.82*(ma.log10(float(self.Htx4.get())))-self.Ahm2 +(44.9-6.55*(ma.log10(float(self.Htx4.get()))))*(ma.log10(float(self.Distancia5.get())))+self.Cm
                    self.Resultado5["text"] = "Lb = "+str(self.lb5)
                    print(self.Ahm2)
                elif self.Var5.get() == 'Grandes Metropolis':
                    self.Cm = 3
                    if float(self.Frecuencia5.get())<= 200:
                        self.Ahm2 = (8.29*ma.pow(ma.log10(1.54*float(self.Ham3.get())), 2))-1.1 
                        self.lb5 = 46.3 + 33.9*(ma.log10(float(self.Frecuencia5.get())))-13.82*(ma.log10(float(self.Htx4.get())))-self.Ahm2 +(44.9-6.55*(ma.log10(float(self.Htx4.get()))))*(ma.log10(float(self.Distancia5.get())))+self.Cm
                        self.Resultado5["text"] = "Lb = "+str(self.lb5)   
                    else:
                        self.Ahm2 = (3.2*ma.pow(ma.log10(11.75*float(self.Ham3.get())), 2))-4.97
                        self.lb5 = 46.3 + 33.9*(ma.log10(float(self.Frecuencia5.get())))-13.82*(ma.log10(float(self.Htx4.get())))-self.Ahm2 +(44.9-6.55*(ma.log10(float(self.Htx4.get()))))*(ma.log10(float(self.Distancia5.get())))+self.Cm
                        self.Resultado5["text"] = "Lb = "+str(self.lb5)
                else:
                    self.mensaje5["text"]="¡ ERROR ! SELECCIONE EL TAMAÑO DE LA CIUDAD"
            else:
                self.mensaje5["text"]="¡ ERROR ! LOS DATOS INGRESADOS NO SON APTOS PARA EL METODO"           
            
        else:
            self.mensaje5["text"] = "¡ ERROR ! RELLENA LOS DATOS"               

        
        

if __name__ == '__main__': 
    #Definir Ventana    
    Ventana = tkinter.Tk()   
    Ventana.title('LAB-4') #Titulo de la app
    Ventana.iconbitmap('unimag.ico') #Icono de la app
    Ventana.geometry('900x650') #Geomeria de la app
    app = Software(Ventana)
    Ventana.mainloop()


