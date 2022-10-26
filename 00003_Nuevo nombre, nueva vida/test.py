class Test(unittest.TestCase):
  def test_se_renombro_loc_code(self):
    self.assertFalse("loc_code" in cines, "ya no debería existir la columna loc_code")
    self.assertTrue("city_id" in cines, "ahora debería existir la columna city_id")
  
  def test_se_renombro_prov_id(self):
    self.assertFalse("prov_id" in cines, "ya no debería existir la columna prov_id")    
    self.assertTrue("province_id" in cines, "ahora debería existir la columna province_id")    
    
  def test_se_renombro_dep_id(self):
    self.assertFalse("dep_id" in cines, "ya no debería existir la columna dep_id")
    self.assertTrue("department_id" in cines, "ahora debería existir la columna department_id")