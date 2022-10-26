class Test(unittest.TestCase):
  def test_loc_code_foi_renomeada(self):
    self.assertFalse("loc_code" in cines, "a coluna loc_code não deve mais existir")
    self.assertTrue("city_id" in cines, "column city_id deve existir agora")

  def test_prov_id_foi_renomeada(self):
    self.assertFalse("prov_id" in cines, "coluna prov_id não deve mais existir")
    self.assertTrue("province_id" in cines, "a coluna província_id deve existir agora")
  
  def test_dep_id_foi_renomeada(self):
    self.assertFalse("dep_id" in cines, "coluna dep_id não deve mais existir")
    self.assertTrue("department_id" in cinemas, "a coluna department_id deve existir agora")