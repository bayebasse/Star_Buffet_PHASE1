from django import forms

class ContactForm(forms.Form):

   name = forms.CharField(
       label="Nom complet",
       max_length=100,
       widget=forms.TextInput(attrs={'placeholder': 'Entrez votre nom'}) # Widget pour personnaliser l'input HTML
   )

   email = forms.EmailField(
       label="Email",
       widget=forms.EmailInput(attrs={'placeholder': 'nom@example.com'})
   )

   # Champ texte long, utilise un <textarea> HTML
   message = forms.CharField(
       label="Description",
       widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Un peu de vous...'}),
       help_text="Soyez aussi précis que possible." # Texte d'aide affiché sous le ch
   )