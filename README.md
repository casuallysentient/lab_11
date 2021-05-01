## CS-UY 1114 — Lab 11
# Object-Oriented Programming
#### April 30th, 2021


**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.


Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab. **The points awarded by the auto-grader on GradeScope will not be counted
towards your lab's grade, so don't worry if you don't pass every or any of its tests!**


Please do not hesitate to check with your TAs if you are ever confused as to how to proceed!

---

### Important Note on Lab Collaboration

While discussion of the lab problems is allowed amongst students in the course, when it is time to implement your
solution, the code must be **entirely** your own work. Submitting code that has been written by someone other than
yourself will, at a minimum, result in receiving a 0 on the lab assignment. Other possible penalties include having
the incident reported to the Office of Student Affairs to be added to your official academic record and/or failing the
course.


---
### I _love_ object-oriented programming.

In my opinion, it is the topic (in this class, anyway) that most accurately
represents how we can combine the power of all the concepts and structures that we've learned so far to create
real-world programs. In this lab, we'll be building a very small game based on dueling. Feel free to expand on
it in your free time and make it as complicated as you like! As long as the methods that we ask for below work,
the auto-grader won't mind.

---

### A couple of ***very important*** notes on this lab.

- This lab is very similar to one that was administered last semester. I like to believe that nobody has been using a
former 1114 student's solutions in order to complete their own labs, but as plagiarism has been a severe problem in
academia in general given our online situation, I'll at least say this: ***Try the lab by yourself.*** Of course, we're
here to answer your questions, but I've instructed the TAs to be extra attentive to finding solutions that strongly
resemble the solutions from last semester (and this involves changing variable names and spacing. Code similarity
software is smarter than that), so if they find this being the case in any submissions, you run a heavy risk of getting
a zero in this lab, or worse if we find more instances of this in your previous labs. This is for your own good,
honestly. Being able to do this lab by yourself is the most basic assurance you can give yourself of doing well in the
final exam, which will undoubtedly be more difficult than this.

- Since a couple of the methods required in this lab have elements of randomness, the auto-grader will be basing its
results on the **probability** of your methods landing on a certain result. I'll try my best to make it so that the
results have an even distribution, but if you see some behavior in the auto-grader that doesn't look right/make sense,
don't hesitate to bring it up with your lab TAs or to email me at [**src402@nyu.edu**](src402@nyu.edu).

— Sebastián.

---

### Problem 1: _It's dangerous to go alone. Take this!_

Our first step is to define a **`Weapon`** class, which will represent the swords that our duelists will be using in
their duels. We'll go method-by-method to make sure everything is covered. Please make sure you understand how each
method is working before moving to the next! All of our code for this lab will go in the file [**duel.py**](duel.py).

#### 1.1: The **`__init__()`** Method

As with most class definitions, we'll start with the constructor, or the **`__init__()`**. Our **`__init__()`**
will accept two parameters from the user:

| **Attribute** | **Type**  | **Comments**                                                   |
|---------------|-----------|----------------------------------------------------------------|
| `weapon_name` | _`str`_   | The name of our weapon.                                        |
| `strength`    | _`float`_ | It's strength value, represented by a `float` from 0.0 to 1.0. |

_**Table 1**: Attributes of the **`Weapon`** class._

Please make sure the spelling of your attributes matches those given in Table 1.

If you implement your initializer method correctly, your **`Weapon`** objects should behave as follows:

```python
def main():
   some_weapon = Weapon("Master Sword", 0.99)
   print(some_weapon.weapon_name)
   print(some_weapon.strength)

main()
```
Output:
```text
Master Sword
0.99
```

#### 1.2: The **`__str__()`** Method

Let's get this one out of the way first. You goal is to simply make sure that the following behavior occurs using the
**`__str__()`** method:

```python
def main():
   some_weapon = Weapon("naginata", 0.75)
   print(some_weapon)

main()
```
Output:
```text
'naginata' Weapon object (strength: 0.75).
```

The auto-grader requires the string that **`__str__()`** returns to be formatted ***exactly*** as the example above
(i.e. same capitalization, spacing, and punctuation. Obviously the values of the weapon's name and attack can change.)

#### 1.3: The **`does_break()`** Method

This is where the random element comes in. This function will simply do the following:
- If a randomly-generated float value from 0.0 to 1.0 is **smaller** than 1/2 of the `strength` attribute of this
**`Weapon`** object, **`does_break()`** will return `True`, meaning the weapon has broken.
- Otherwise, return `False`, meaning the weapon has stood the test of time and not broken.

That is, the stronger a **`Weapon`** object is, the more likely it is to break.

Consider the following *possible* sample behavior:

```python
def main():
   some_weapon = Weapon("Rickenbacker 4003", 0.6)
  
   number_of_tests = 100
   number_of_breaks = 0

   # I'm testing this 100 times and keeping track of how many times it breaks
   for i in range(number_of_tests):
       if some_weapon.does_break():
           number_of_breaks += 1
  
   percentage = (number_of_breaks / number_of_tests) * 100

   print("The {} broke {}% of the time in {} tests!".format(some_weapon.weapon_name, round(percentage),
         number_of_tests))

main()
```
_Possible_ output:
```text
The Rickenbacker 4003 broke 23% of the time in 100 tests!
```

That's it for the **`Weapon`** class. Please make sure you understand and have gotten it to work perfectly before
moving on to the next part, as we'll be making use of **`Weapon`** objects!

### Problem 2: _There's something I ought to tell you—I'm not left-handed either._

Next up, we'll be creating our duelists; the class will be called **`Duelist`**, and will contain the following methods:

#### 2.1: The **`__init__()`** Method

Similar to our **`Weapon`** class, define the constructor for our **`Duelist`** class, which will contain the following
attributes:

| **Attribute**      | **Type**     | **Comments**                                  |
|--------------------|--------------|-----------------------------------------------|
| `duelist_name`     | _`str`_      | The name of our duelist.                      |
| `weapon_inventory` | _`[Weapon]`_ | That is, a list of ***3*** `Weapon` objects. |

_**Table 2**: Attributes of the **`Duelist`** class._

Please make sure the spelling of your attributes matches those given in Table 2.

The `weapon_inventory` attribute will have to be created by you inside the **`__init__()`** method, from ***three***
weapon objects that the user will use to initialize each **`Duelist`** objects. You may assume the user will always
pass in three `Weapon` objects after `duelist_name`.

If you implement your constructor correctly, your **`Duelist`** objects should behave as follows:

```python
def main():
   # Creating our 3 Weapon objects first
   some_weapon = Weapon("Master Sword", 0.99)
   another_weapon = Weapon("Kokiri Sword", 0.4)
   a_final_weapon = Weapon("Biggoron's Sword", 0.75)
  
   # Creating our Duelist object using the 3 Weapon objects we created above
   sample_duelist = Duelist("Link", some_weapon, another_weapon, a_final_weapon)
  
   print(sample_duelist.duelist_name)
   for weapon in sample_duelist.weapon_inventory:
       print(weapon)  # we can do this because weapon_inventory is a list

main()
```
Output:
```text
Link
'Master Sword' Weapon object (strength: 0.99).
'Kokiri Sword' Weapon object (strength: 0.4).
'Biggoron's Sword' Weapon object (strength: 0.75).
```

#### 2.2: The **`__str__()`** Method

This one should be quick. Implement the **`Duelist`** class's **`__str__()`** method so that you get the following
behavior:

```python
def main():
   some_weapon = Weapon("Master Sword", 0.99)
   another_weapon = Weapon("Kokiri Sword", 0.4)
   a_final_weapon = Weapon("Biggoron's Sword", 0.75)
  
   sample_duelist = Duelist("Link", some_weapon, another_weapon, a_final_weapon)
  
   print(sample_duelist)

main()
```
Output:
```text
Duelist object 'Link', carrying Master Sword, Kokiri Sword, and Biggoron's Sword Weapon objects.
```

Remember that the auto-grader requires the string that **`__str__()`** returns to be formatted ***exactly*** as the
example above (i.e. same capitalization, spacing, and punctuation. Obviously the values of the duelist's name and
weapons can change.)

#### 2.3: The **`get_winner_of_duel_name()`** Method

Our last method will be called **`get_winner_of_duel_name()`**, and it will do the following:

- Accept one parameter (other than _`self`_, that is), `opponent`, which you can assume will always be another `Duelist`
object.
- The method will then pick a random `Weapon` object from each of the `Duelist` objects in this duel (that is, one from
the `Duelist` object that called the **`get_winner_of_duel_name()`** method, and one from the `Duelist` object that was
passed into it). You may assume that both `Duelist` objects will have at least one `Weapon` inside their
`weapon_inventory` attribute.
- Finally, **`get_winner_of_duel_name()`** will do something very similar to what we did in midterm 2 from last
semester, in case you used it to study this semester. First, check which `Weapon` object's `strength` attribute is
larger. Let's say Duelist A's weapon is stronger than Duelist B's. If so, our program will call Duelist ***A***'s
`Weapon` object's `does_break()` method. If it returns `True` (that is, if it breaks), Duelist B wins in an upset. If
Duelist B's weapon was stronger than Duelist A's, we do the same process, but instead calling Duelist ***B***'s `Weapon`
object's `does_break()` method. If both `Weapon` objects happen to have the same `strength` value, the winner will be
decided by a 50/50 random coin-toss. **Whichever `Duelist` wins, return their `duelist_name` attribute**.

**WARNING**: When picking `Weapon` objects from each `Duelist` object in the duel, make sure not to remove it from that
`Duelist` object's `weapon_inventory` list. In other words, each `Duelist` object's `weapon_inventory` list must never
change once it is initialized.

If you successfully implement this method, you should see similar behavior to the following, very
[***FLCL***](https://en.wikipedia.org/wiki/List_of_FLCL_characters#Haruko_Haruhara), example. I added a few `print()` 
function calls in my **`get_winner_of_duel_name()`** method to better illustrate what is happening behind the scenes. 
Feel free to do this as well if it helps you:

```python
def main():
   # Creating my Weapon objects
   weapon_1 = Weapon("Rickenbacker 4001c64", 0.8)
   weapon_2 = Weapon("Hofner 500/1", 0.6)
   weapon_3 = Weapon("Squier VI", 0.4)

   weapon_4 = Weapon("Rickenbacker 330", 0.8)
   weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
   weapon_6 = Weapon("Gretsch 6122", 0.4)

   # Creating my Duelist objects
   bass_player = Duelist("Aki Mizuguchi", weapon_1, weapon_2, weapon_3)
   guitarist = Duelist("Yori Asanagi", weapon_4, weapon_5, weapon_6)

   # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
   number_of_duels = 10

   for duel_number in range(number_of_duels):
       winner = bass_player.get_winner_of_duel_name(guitarist)
       print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")

main()
```
_Possible_ output (notice the duels wherein `Weapon` objects "break" and/or have the same value for `strength`):
```text
Duelist Aki Mizuguchi picked a Hofner 500/1!
Duelist Yori Asanagi picked a Fender Vintera 60s Mustang!
Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generated fate!
THE WINNER OF DUEL #1 IS Yori Asanagi!

Duelist Aki Mizuguchi picked a Squier VI!
Duelist Yori Asanagi picked a Fender Vintera 60s Mustang!
Yori Asanagi's Fender Vintera 60s Mustang broke!
THE WINNER OF DUEL #2 IS Aki Mizuguchi!

Duelist Aki Mizuguchi picked a Squier VI!
Duelist Yori Asanagi picked a Rickenbacker 330!
THE WINNER OF DUEL #3 IS Yori Asanagi!

Duelist Aki Mizuguchi picked a Squier VI!
Duelist Yori Asanagi picked a Gretsch 6122!
Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generated fate!
THE WINNER OF DUEL #4 IS Yori Asanagi!

Duelist Aki Mizuguchi picked a Rickenbacker 4001c64!
Duelist Yori Asanagi picked a Fender Vintera 60s Mustang!
THE WINNER OF DUEL #5 IS Aki Mizuguchi!

Duelist Aki Mizuguchi picked a Hofner 500/1!
Duelist Yori Asanagi picked a Rickenbacker 330!
THE WINNER OF DUEL #6 IS Yori Asanagi!

Duelist Aki Mizuguchi picked a Hofner 500/1!
Duelist Yori Asanagi picked a Gretsch 6122!
THE WINNER OF DUEL #7 IS Aki Mizuguchi!

Duelist Aki Mizuguchi picked a Rickenbacker 4001c64!
Duelist Yori Asanagi picked a Rickenbacker 330!
Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generated fate!
THE WINNER OF DUEL #8 IS Aki Mizuguchi!

Duelist Aki Mizuguchi picked a Rickenbacker 4001c64!
Duelist Yori Asanagi picked a Rickenbacker 330!
Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generated fate!
THE WINNER OF DUEL #9 IS Yori Asanagi!

Duelist Aki Mizuguchi picked a Hofner 500/1!
Duelist Yori Asanagi picked a Gretsch 6122!
THE WINNER OF DUEL #10 IS Aki Mizuguchi!
```

