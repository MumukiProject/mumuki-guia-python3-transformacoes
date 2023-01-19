import numpy as np

class Test(unittest.TestCase):
  def setUp(self):
    self.indexado = visitas_previas_por_regiao.set_index("region")
  
  def test_visitas_previas_por_regiao_e_um_DataFrame(self):
    self.assertEquals(type(visitas_previas_por_regiao), pd.DataFrame)

  def test_contem_coluna_region_e_average_previous_visits(self):
    self.assertEquals(list(visitas_previas_por_regiao.columns), ['region', 'average_previous_visits'])

  def test_contem_3_linhas(self):
    self.assertEquals(len(visitas_previas_por_regiao), 3)

  def test_contem_a_media_nacional(self):
    self.assertTrue(self.indexado.loc["Nacional", "average_previous_visits"] == 5.0)
    
  def test_contem_a_media_regional(self):
    self.assertTrue(self.indexado.loc["Regional", "average_previous_visits"] == 1.25)
    
  def test_contem_a_media_não_regional(self):
    self.assertTrue(self.indexado.loc["Não regional", "average_previous_visits"] == 0.5)            