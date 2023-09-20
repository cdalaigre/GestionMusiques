from django.test import TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from musiques.models import Morceau,Artiste

# Create your tests here.
class MorceauTestCase(TestCase):

    def setUp(self):
        Artiste.objects.create(nom="artisteTest")
        artiste = Artiste.objects.get(nom="artisteTest")
        Morceau.objects.create(titre='musiqueTest', fk_artiste=artiste)
   
        
    def test_morceau_url_name(self):
        try:
            url = reverse('morceau-detail', args=[1])
        except NoReverseMatch:
            assert False

    def test_morceau_url(self):
        morceau = Morceau.objects.get(titre='musiqueTest')
        url = reverse('morceau-detail', args=[morceau.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        