class FieldModel
{
  public ArrayList<Human> objects = new ArrayList<Human>(100);
  public int K_NEAREST_NEIGHBOURS = 5;

  //     !!!ALGORITHM!!!
  public void addHuman(Human h)
  {
    h.cluster = getHumanClusterOriginal(h);
    objects.add(h);
  }
  
  public int getHumanClusterOriginal(Human h)
  {
     ArrayList<Human> closest = getNClosest(h,objects,K_NEAREST_NEIGHBOURS);
     switch(closest.size())
     {
       case 0: return 0;
       case 1: return closest.get(0).cluster;
     }
     double step = 1.0 / (closest.size() + 1);
     double currW = 1 - step;
     HashMap<Integer, Double> weights = new HashMap<Integer, Double>();
     //count sum of all weights
     for(Human human : closest)
     {
       //System.out.println(currW);
       double newW = weights.getOrDefault(human.cluster, new Double(0)) + currW;
       weights.put(human.cluster, newW);
       currW -= step;
     }
     //lookup most important cluster
     int maxCluster = 0;
     int maxValue = 0;
     for(Integer i : weights.keySet()) //i is a cluster number
     {
       if(weights.get(i) > maxValue)
       {
         maxCluster = i;
       }
     }
     return maxCluster;
  }

  public void addCluster(Human h)
  {
    objects.add(h);
  }
  
  public void drawModel()
  {
    for(Human h : objects)
    {
      h.draw();
    }
  }
}

int range = 75;
ArrayList<Human> getDataSet(int x, int y, int cluster)
{
  ArrayList<Human> res = new ArrayList<Human>();
  int amount = (int)random(10,20);
  for(int i = 0; i < amount;++i)
  {
    Human h = new Human(x+(int)random(-range,range),y+(int)random(-range,range));
    h.cluster = cluster;
    res.add(h);
  }
  return res;
}

int lossFunction(FieldModel model, ArrayList<Human> list)
{
  int losses = 0;
  for(Human h : list)
  {
    if(model.getHumanClusterOriginal(h) != h.cluster)
    {
      losses += 1;
    }
  }
  return losses;
}