# This is Andy's Solution. You should read through the code if 
# you're feeling stuck or if you're just interested in one way
# to solve the problem.
#
# You're page is probably using a different HTML structure.
# If that's the case, you may want to modify the 
# generate_concept_HTML function to better suit your HTML.
def generate_section_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="section">
    <div class="sectionTitle">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="content">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept [0]
    concept_description = concept[1]
    return generate_section_HTML(concept_title, concept_description)

List_of_lessons = [["Computer Program","Computers can be programed to do anything you need them to as long as you give them specific instructions on what needs to be done. You do this by giving me a precise sequence of steps that it can follow to do what you need it to do."],
                    ["Python & Python Expressions","Python is an interpreter that takes the written code and produces an output specific to the input or code written. Specific instructions need to be given in order for Python to be able to produce an output.  If there is something not clear (for example 2 + 2 +) then it does not have the ability to speculate what outcome your were looking for (like 2 + 2)."],
                    ["Phython: Variables and Strings","In Python you use a = to assigne a value to a variable."],
                ["Differences in using Variables","On the other hand if you assign the variable a number value like number=2 and then did print number + number you would get an outcome of 4. If you put quote marks around the variable like a number, it is no longer considered a number. so number=&quot2&quot and prnt number + number you would get an outcome of 22. In Python saying somehting + something else does not always refer to acctual addition as in math, but adding/combining two Variables depending on what the variables values are."],
                    ["Function?","What is a function in programing? A function takes an input and then produces an output. In order to write this in start with keyword  followed by a function name and the function paramater in parentheses. What is in the parentheses will end being replaced by the actual value in the function when it is used. For example if you wanted to square of a number you could write the following:<br>Retrun vs Print: Without a return statement the code really isn't doing anything even though it may print something out in text.  To make a function whole and complete you should end with a return statement."],
                    ["When and how are they used?","An if statement is used to determine which set of codes is to be used. For example if x = 5 then multiply by 10, else mulitply by 2. While loops on the other hand repeart until a criteria/condition is met. For example while the date is less than 15 add $2 to x.  The code will continue until the date is no longer less than 15 and will continue to perform the function of adding $2."],
                    ["How to Solve Problems","There are two key components when it comes to solving problems: <b>input</b> and <b>output</b>. Understanding the inputs and outputs of anything will help you better underdtand how it works and resolve any potention problem.  This is the same for coding and if you come accross any issue executing the code. Knowing and understanding your inputs and outputs of any code are key to help determine any potential issue when the code does not work as expected."]]



def make_all_HTML(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_all_HTML(List_of_lessons)

