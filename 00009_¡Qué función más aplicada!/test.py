class Test(unittest.TestCase):

  def test_cruceristas_contiene_la_columna_estimated_foreign_income(self):
    self.assertTrue("estimated_foreign_income" in cruceristas)
    
  def test_cruceristas_de_uruguay_tienen_ingreso_estimado_cero(self):
    self.assertEquals(cruceristas.set_index("cruise_id").loc[5823, "estimated_foreign_income"], 0, "crucerista 5823 debería tener estimated_foreign_income en 0")    
    
  def test_cruceristas_de_brasil_tienen_ingreso_estimado_no_cero(self):
    self.assertEquals(cruceristas.set_index("cruise_id").loc[7404, "estimated_foreign_income"], 224.76, "crucerista 7404 debería tener estimated_foreign_income en 224.76")
    
  def test_cruceristas_de_otro_pais_de_asia_tienen_ingreso_estimado_no_cero(self):
    self.assertEquals(int(cruceristas.set_index("cruise_id").loc[7638, "estimated_foreign_income"]), 125, "crucerista 7638 debería tener estimated_foreign_income en 125 aproximadamente")
    
