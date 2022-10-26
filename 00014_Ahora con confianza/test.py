import numpy as np

class Test(unittest.TestCase):
  def setUp(self):
    self.indexado = visitas_previas_por_region.set_index("region")
  
  def test_visitas_previas_por_region_es_un_DataFrame(self):
    self.assertEquals(type(visitas_previas_por_region), pd.DataFrame)

  def test_contiene_columnas_region_y_average_previous_visits(self):
    self.assertEquals(list(visitas_previas_por_region.columns), ['region', 'average_previous_visits'])

  def test_contiene_3_filas(self):
    self.assertEquals(len(visitas_previas_por_region), 3)

  def test_contiene_el_promedio_nacional(self):
    self.assertTrue(self.indexado.loc["Nacional", "average_previous_visits"] == 5.0)
    
  def test_contiene_el_promedio_regional(self):
    self.assertTrue(self.indexado.loc["Regional", "average_previous_visits"] == 1.25)
    
  def test_contiene_el_promedio_no_regional(self):
    self.assertTrue(self.indexado.loc["No regional", "average_previous_visits"] == 0.5)            