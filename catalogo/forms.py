from django import forms

from . models import Producto,Marca



class ProductoForm(forms.ModelForm):


    nombre = forms.CharField(label='Nombre', 
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(),label='Marca',  
        widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    modelo = forms.CharField(label='Descripción',  
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    precio = forms.IntegerField (label='Género',
            widget=forms.NumberInput(
            attrs={
                'class':'form-control' 
            }
            ))
    color = forms.CharField(label='Descripción',required=False,
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    peso = forms.DecimalField(label='Descripción',required=False,
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    alto = forms.DecimalField(label='Descripción',required=False,
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    ancho = forms.DecimalField(label='Descripción',required=False,  
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    img1 = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    img2 = forms.ImageField(label='Imagen',required=False,
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    img3 = forms.ImageField(label='Imagen',required=False,
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    img4 = forms.ImageField(label='Imagen',required=False,
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    class Meta:
        model = Producto
        fields = ('nombre','marca','modelo', 'precio', 'color','peso','alto','ancho','img1','img2','img3','img4')