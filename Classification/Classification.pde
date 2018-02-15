int clusterAmounts = 0;
boolean isClustersAdd = true;
boolean isBattleMode= false;
FieldModel model = new FieldModel();

void addNewCluster(int x, int y, int cluster)
{
  for(Human h : getDataSet(x, y, cluster))
  {
    model.addCluster(h);
  }
}

ArrayList<Human> createTrainDataset()
{
  ArrayList<Human> res = new ArrayList<Human>();
  int d = range;
  range = 50;
  res.addAll(getDataSet(70+(int)random(range),70+(int)random(range),0));
  res.addAll(getDataSet(350+(int)random(range),100+(int)random(range),1));
  res.addAll(getDataSet(170+(int)random(range),250+(int)random(range),2));
  res.addAll(getDataSet(400+(int)random(range),450+(int)random(range),3));
  range = d;
  return res;
}

void setup()
{
  size(500,500);
  background(255,255,255);
  addNewCluster(70,70,0);
  addNewCluster(350,100,1);
  addNewCluster(170,250,2);
  addNewCluster(400,450,3);
  ArrayList<Human> dataset = createTrainDataset();
  int elem = 0;
  int loss = model.objects.size();
  for(int i = model.objects.size(); i > 0; --i)
  {
    model.K_NEAREST_NEIGHBOURS = i;
    int lost = lossFunction(model, dataset);
    System.out.println("Loss for K = " + i + " is " + lost + " elements");
    if(lost < loss)
    {
      elem = i;
      loss = lost;
    }
  }
  System.out.println("Optimal K = "+elem);
}

void draw()
{
  model.drawModel();
}

void mouseClicked(MouseEvent event)
{
  Human h = new Human(event.getX(), event.getY());
  if(event.getButton() == LEFT && isClustersAdd)
  {
    h.cluster = clusterAmounts;
    model.addCluster(h);
  }
  else if(event.getButton() == LEFT && !isClustersAdd) 
  {
    if(isBattleMode)
    {
      model.addHuman(h);
    }
    else
    {
      h.cluster = clusterAmounts;
      model.addCluster(h);
    }
  }
  else if(event.getButton() == RIGHT)
  {
    isClustersAdd = !isClustersAdd;
    if(isClustersAdd)
    {
      stroke(250,0,0);
    }
    else
    {
      stroke(0,0,0);
    }
    System.out.println(isClustersAdd ? "Adding clusters mode" : (isBattleMode ? "Classify mode" : "Adding points mode"));
  }
}

void keyReleased(KeyEvent event)
{
  if(event.getKey() == 'b')
  {
    isBattleMode = !isBattleMode;
    System.out.println(isBattleMode ? "Battle mode active" : "Battle mode disabled");
  }
  else if(event.getKey() == 'n')
  {
    clusterAmounts++;
    System.out.println("Using cluster #"+clusterAmounts);
  }
  else if(event.getKey() == 'p')
  {
    clusterAmounts--;
    System.out.println("Using cluster #"+clusterAmounts);
  }
}