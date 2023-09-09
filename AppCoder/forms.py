from django import forms

class formularioC(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class formularioE(forms.Form):   
    origen= forms.CharField(max_length=40)
    destino= forms.CharField(max_length=40)
    numero = forms.IntegerField()
    producto= forms.CharField(max_length=40)

class formularioP(forms.Form):   
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    cantidad = forms.IntegerField()



