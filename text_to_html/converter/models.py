from django.db import models

class TextToHTML(models.Model):
    text = models.TextField()  # Kullanıcının girdiği metin
    html = models.TextField()  # HTML'e dönüştürülmüş metin
    created_at = models.DateTimeField(auto_now_add=True)  # Kaydın oluşturulma zamanı

    def __str__(self):
        return f"TextToHTML(id={self.id})"
