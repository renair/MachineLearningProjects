class Human
{
  //parameters
  public int age;
  public int strength;
  public int intelligence;
  //for models
  public int cluster;
  
  public Human(int age, int intelligence)
  {
    this.age = age;
    this.intelligence = intelligence;
  }
  
  public Human(int age, int strength, int intelligence)
  {
    this.age = age;
    this.strength = strength;
    this.intelligence = intelligence;
  }
  
  public void draw()
  {
    fill(getColor(cluster));
    ellipse(age,intelligence,20,20);
  }
  
  public double distance2d(Human h)
  {
    return sqrt(pow(h.age-this.age,2)+pow(h.intelligence-this.intelligence,2));
  }
  
  public double distance3d(Human h)
  {
    return sqrt(pow(h.age-this.age,2)+pow(h.strength-this.strength,2)+pow(h.intelligence-this.intelligence,2));
  }
}

//non class methods for algorithm
ArrayList<Human> getNClosest(Human start, ArrayList<Human> others, int N)
{
  ArrayList<Human> result = new ArrayList<Human>(N);
  Human[] humans = new Human[others.size()];
  others.toArray(humans);
  sortArray(start,humans);
  for(int i = 0;i < N && i < humans.length;++i)
  {
    result.add(humans[i]);
  }
  return result;
}

void sortArray(Human h, Human[] arr)
{
  for(int i = 0; i < arr.length;++i)
  {
    for(int q = i+1; q < arr.length-1;++q)
    {
      if(h.distance2d(arr[i]) > h.distance2d(arr[q]))
      {
        Human tmp = arr[i];
        arr[i] = arr[q];
        arr[q] = tmp;
      }
    }
  }
}