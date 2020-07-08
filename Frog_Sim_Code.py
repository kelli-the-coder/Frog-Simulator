import pygame
from pygame.locals import *
import random
import Frog_Sim_DB_code as DB

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Frog Simulator")

male_frog = pygame.image.load("Pictures/male_frog.png")
female_frog = pygame.image.load("Pictures/female_frog.png")
mad_frog = pygame.image.load("Pictures/mad_frog2.png")
fly = pygame.image.load("Pictures/Fly.png")
beetle = pygame.image.load("Pictures/beetle.png")
grasshopper = pygame.image.load("Pictures/grasshopper.png")
daphne = pygame.image.load("Pictures/daphne.png")
tiana = pygame.image.load("Pictures/tiana.png")
mary = pygame.image.load("Pictures/mary.png")
todd = pygame.image.load("Pictures/todd.png")
ben = pygame.image.load("Pictures/ben.png")
ethan = pygame.image.load("Pictures/ethan.png")
rose1 = pygame.image.load("Pictures/roses.png")
tadpole = pygame.image.load("Pictures/tadpole.png")
birth_certificate = pygame.image.load("Pictures/Birth_Certificate.png")

class Frog:
    def __init__(self, gender, name, health=50, mate="single", offsprings=[]):
        self.name = name
        self.gender = gender
        self.health = health
        self.mate = mate
        self.offsprings = offsprings

    def __repr__(self):
        return "Name: " + self.name + " Gender: " + self.gender + " Health: " + str(self.health) + \
            " Mate: " + self.mate + " Offsprings: " + str(self.offsprings)

    def eat(self):
        fly_box_color = (126, 217, 119)
        beetle_box_color = (126, 217, 119)
        grasshopper_box_color = (126, 217, 119)
        eat_on = True
        directions = True
        choose_insect = False
        actual_game = False
        chosen_bug = "unknown"
        game_iteration = 0
        lag = 0
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        while eat_on:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)
            screen.fill((126, 217, 119))

            if directions:
                welcome_font = pygame.font.SysFont('juiceitc', 50)
                welcome_text = welcome_font.render("Welcome to the Food Game", 1, (0, 0, 0))
                screen.blit(welcome_text, welcome_text.get_rect(centerx=400, centery=70))

                direc_font = pygame.font.SysFont('impact', 30)
                direc_text1 = direc_font.render("Click the insect to catch it! But ya gotta be quick!", 1, (0, 0, 0))
                direc_text2 = direc_font.render("Choose a harder insect to get more health.", 1, (0, 0, 0))
                screen.blit(direc_text1, direc_text1.get_rect(centerx=400, centery=200))
                screen.blit(direc_text2, direc_text2.get_rect(centerx=400, centery=250 ))

                start_button = pygame.draw.rect(screen, (0, 0, 0), (330, 300, 150, 70))
                start_button_text = button_text_font.render("START", 1, (0, 255, 0))
                screen.blit(start_button_text, (start_button[0]+27, start_button[1]+10))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        if start_button.colliderect(mouse_pos):
                            directions = False
                            choose_insect = True

            elif not directions and choose_insect:
                #this is where the  person will pick what insect

                choose_insect_text = title_font.render("Choose which insect", 1, (0, 0, 0))
                screen.blit(choose_insect_text, (250, 30))

                fly_dim = fly.get_rect(centerx=130, centery=250)
                pygame.draw.rect(screen, fly_box_color, fly_dim)
                screen.blit(fly, fly_dim)

                beetle_dim = beetle.get_rect(centerx=410, centery=250)
                pygame.draw.rect(screen, beetle_box_color, beetle_dim)
                screen.blit(beetle, beetle_dim)

                grasshopper_dim = grasshopper.get_rect(centerx=680, centery=250)
                pygame.draw.rect(screen, grasshopper_box_color, grasshopper_dim)
                screen.blit(grasshopper, grasshopper_dim)

                insect_name_font = pygame.font.SysFont("impact", 40)
                info_font = pygame.font.SysFont("impact", 20)

                fly_text = insect_name_font.render("Fly", 1, (0, 0, 0))
                fly_health_text = info_font.render("5 health points", 1, (0, 0, 0))
                screen.blit(fly_text, fly_text.get_rect(centerx=130, centery=390))
                screen.blit(fly_health_text, fly_health_text.get_rect(centerx=130, centery=430))

                beetle_text = insect_name_font.render("Beetle", 1, (0, 0, 0))
                beetle_health_text = info_font.render("7 health points", 1, (0, 0, 0))
                screen.blit(beetle_text, beetle_text.get_rect(centerx=400, centery=390))
                screen.blit(beetle_health_text, beetle_health_text.get_rect(centerx=400, centery=430))

                grasshopper_text = insect_name_font.render("Grasshopper", 1, (0, 0, 0))
                grasshopper_health_text = info_font.render("10 health points", 1, (0, 0, 0))
                screen.blit(grasshopper_text, grasshopper_text.get_rect(centerx=680, centery=390))
                screen.blit(grasshopper_health_text, grasshopper_health_text.get_rect(centerx=680, centery=430))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    if event.type == MOUSEMOTION:
                        if fly_dim.colliderect(mouse_pos):
                            fly_box_color = (6, 186, 0)
                        else:
                            fly_box_color = (126, 217, 119)

                        if beetle_dim.colliderect(mouse_pos):
                            beetle_box_color = (6, 186, 0)
                        else:
                            beetle_box_color = (126, 217, 119)

                        if grasshopper_dim.colliderect(mouse_pos):
                            grasshopper_box_color = (6, 186, 0)
                        else:
                            grasshopper_box_color = (126, 217, 119)
                    if event.type == MOUSEBUTTONDOWN:
                        if fly_dim.colliderect(mouse_pos):
                            chosen_bug = fly
                            choose_insect = False
                            actual_game = True
                        elif beetle_dim.colliderect(mouse_pos):
                            chosen_bug = beetle
                            choose_insect = False
                            actual_game = True
                        elif grasshopper_dim.colliderect(mouse_pos):
                            chosen_bug = grasshopper
                            choose_insect = False
                            actual_game = True

            elif not directions and not choose_insect and actual_game:
                game_iteration += 1

                if chosen_bug == fly:
                    lag = 150
                    hp = 5
                    #hitbox = fly.get_rect()
                elif chosen_bug == beetle:
                    lag = 100
                    hp = 7
                    #hitbox = beetle.get_rect()
                elif chosen_bug == grasshopper:
                    lag = 50
                    hp = 10
                    #hitbox = grasshopper.get_rect()

                if game_iteration % lag == 0:
                    x = random.randint(-100, 800)
                    y = random.randint(-100, 500)
                    screen.blit(chosen_bug, (x, y))
                else:
                    screen.blit(chosen_bug, (x, y))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if (chosen_bug.get_rect(x=x, y=y)).colliderect(mouse_pos):
                            actual_game = False
                            self.health += hp
                            if self.health > 100:
                                self.health = 100
            else:

                good_job_text = title_font.render("Good Job!", 1, (0, 0, 0))
                screen.blit(good_job_text, good_job_text.get_rect(centerx=400, centery=70))

                you_won_text = direc_font.render("You won " + str(hp) + " hp!", 1, (0, 0, 0))
                current_health_text = direc_font.render("Your current health is " + str(self.health) + ".", 1, (0, 0, 0))
                screen.blit(you_won_text, you_won_text.get_rect(centerx=400, centery=200) )
                screen.blit(current_health_text, current_health_text.get_rect(centerx=400, centery=250 ))

                menu_button = pygame.draw.rect(screen, (0, 0, 0), (330, 300, 150, 70))
                menu_button_text = button_text_font.render("MENU", 1, (0, 255, 0))
                screen.blit(menu_button_text, (360, 310))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        if menu_button.colliderect(mouse_pos):
                            return

            pygame.display.flip()

    def fight(self):
        directions = True
        actual_game = False
        enemy_health = 50
        won = False
        lost = False
        times = 0
        fight = True
        while fight:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)
            screen.fill((126, 217, 119))

            if directions:
                welcome_font = pygame.font.SysFont('juiceitc', 50)
                welcome_text = welcome_font.render("Welcome to the Fighting Game", 1, (0, 0, 0))
                screen.blit(welcome_text, welcome_text.get_rect(centerx=400, centery=70))

                direc_font = pygame.font.SysFont('impact', 30)
                direc_text1 = direc_font.render("Choose the right spot to hit, or you might get hit yourself!", 1, (0, 0, 0))
                direc_text2 = direc_font.render("Choose the right spot to hit, and your opponet takes 25 damage.", 1, (0, 0, 0))
                direc_text3 = direc_font.render("But if it's the wrong spot, you take 25 damage.", 1, (0, 0, 0))
                screen.blit(direc_text1, direc_text1.get_rect(centerx=400, centery=170))
                screen.blit(direc_text2, direc_text2.get_rect(centerx=400, centery=220))
                screen.blit(direc_text3, direc_text3.get_rect(centerx=400, centery=270))

                warning_font = pygame.font.SysFont('impact', 40)
                warning_text = warning_font.render("WARNING: if you lose all your health, you will die!", 1, (255, 0, 0))
                screen.blit(warning_text, warning_text.get_rect(centerx=400, centery=320))

                start_button = pygame.draw.rect(screen, (0, 0, 0), (330, 370, 150, 70))
                start_button_text = button_text_font.render("START", 1, (0, 255, 0))
                screen.blit(start_button_text, (start_button[0]+25, start_button[1]+10))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if start_button.colliderect(mouse_pos):
                            directions = False
                            actual_game = True

            elif not directions and actual_game:
                times += 1
                screen.blit(mad_frog, (160, 20))

                health_font = pygame.font.SysFont('impact', 30)
                your_health_text = health_font.render("Your health is: " + str(self.health), 1, (0, 0, 255))
                enemy_health_text = health_font.render("Opponent's health is: " + str(enemy_health), 1, (255, 0, 0))
                screen.blit(your_health_text, (300, 420))
                screen.blit(enemy_health_text, (260, 450))

                arm_hitbox = pygame.draw.rect(screen, (255, 0, 0), (410, 280, 70, 70), 3)
                leg_hitbox = pygame.draw.rect(screen, (255, 0, 0), (550, 190, 70, 70), 3)
                face_hitbox = pygame.draw.rect(screen, (255, 0, 0), (370, 130, 70, 70), 3)

                if times == 1:
                    right_spot = random.choice((arm_hitbox, leg_hitbox, face_hitbox))

                forfeit_button = pygame.draw.rect(screen, (255, 0, 0), (600, 400, 130, 70))
                forfeit_font = pygame.font.SysFont('impact', 35)
                forfeit_text = forfeit_font.render("FORFEIT", 1, (0, 0, 0))
                screen.blit(forfeit_text, (forfeit_button[0]+10, forfeit_button[1]+13))

                if enemy_health <= 0:
                    actual_game = False
                    won = True
                elif self.health <=0:
                    actual_game = False
                    lost = True

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if right_spot.colliderect(mouse_pos):
                            enemy_health -= 25
                        elif not (right_spot.colliderect(mouse_pos)) and (arm_hitbox.colliderect(mouse_pos) or leg_hitbox.colliderect(mouse_pos) or face_hitbox.colliderect(mouse_pos)):
                            self.health -= 25
                        elif forfeit_button.colliderect(mouse_pos):
                            return
            elif won:
                conclusion_font = pygame.font.SysFont('juiceitc', 100)
                you_won_text = conclusion_font.render('YOU WON!!', 1, (0, 0, 0))
                screen.blit(you_won_text, (270, 100))

                health_now_text = health_font.render("Your health is now: " + str(self.health), 1, (0, 0, 255))
                screen.blit(health_now_text, (275, 350))

                menu_button = pygame.draw.rect(screen, (0, 0, 0), (330, 250, 150, 70))
                menu_button_text = button_text_font.render("Menu", 1, (0, 255, 0))
                screen.blit(menu_button_text, (menu_button[0]+30, menu_button[1]+10))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if menu_button.colliderect(mouse_pos):
                            return

            elif not won and lost:
                conclusion_font = pygame.font.SysFont('juiceitc', 100)
                you_died_text = conclusion_font.render("YOU CROAKED", 1, (0, 0, 0))
                screen.blit(you_died_text, (235, 100))

                restart_button = pygame.draw.rect(screen, (0, 0, 0), (330, 250, 150, 70))
                restart_text = button_text_font.render("Restart", 1, (0, 255, 0))
                screen.blit(restart_text, (restart_button[0]+15, restart_button[1]+10))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if restart_button.colliderect(mouse_pos):
                            return "died"

            pygame.display.flip()

    def find_mate(self):
        bachs = {"Mary": mary, "Tiana": tiana, "Daphne": daphne, "Todd": todd, "Ethan": ethan, "Ben": ben}
        if self.gender == "male":

            crush = random.choice(list(bachs.keys())[0:3])
        elif self.gender == "female":
            crush = random.choice(list(bachs.keys())[3:])

        back_color = (126, 217, 119)
        directions = True
        game = False
        score = 0
        time_left = 0
        ticks = 0
        won = False
        lost = False
        find_mate = True
        while find_mate:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)
            screen.fill((126, 217, 119))

            if directions:

                back = pygame.draw.rect(screen, back_color, bachs[crush].get_rect(x=230, y=160))

                screen.blit(bachs[crush], (bachs[crush].get_rect(x=230, y=160)))

                crush_text_font = pygame.font.SysFont('impact', 30)
                crush_text = crush_text_font.render("Looks like " + crush + " likes you!", 1, (0, 0, 0))
                screen.blit(crush_text, (250, 30))
                directions_text = crush_text_font.render("Collect 30 flowers for "+crush.capitalize()+"!",1,(0, 0, 0))
                screen.blit(directions_text, (240, 60))
                start_text = crush_text_font.render("Click on "+crush.capitalize()+" to start",1,(255,0,0))
                screen.blit(start_text, (265, 110))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEMOTION:
                        if (bachs[crush].get_rect(x=230, y=160)).colliderect(mouse_pos):
                            back_color = (6, 186, 0)
                        else:
                            back_color = (126,217,119)

                    if event.type == MOUSEBUTTONDOWN:
                        if (bachs[crush].get_rect(x=230, y=160)).colliderect(mouse_pos):
                            game = True
                            directions = False
                            clock = pygame.time.Clock()
                            ticks = 0

            elif game:
                ticks += clock.tick()
                time_left = 20 - round((ticks / 1000))
                if time_left < 0:
                    if score >= 30:
                        won = True
                        game = False
                    else:
                        lost = True
                        game = False


                coords = [(10, 30), (250, 170), (500, 30), (20, 350), (500, 350)]

                for coord in coords:
                  screen.blit(rose1, coord)

                score_font = pygame.font.SysFont('impact', 30)
                score_text = score_font.render("Score: "+str(score), 1, (0, 0, 0))
                screen.blit(score_text, (360, 50))

                time_text = score_font.render("Time left: " + str(time_left), 1, (0, 0, 0))
                screen.blit(time_text, (320, 100))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        for c in coords:
                            if (rose1.get_rect(x=c[0], y=c[1])).colliderect(mouse_pos):
                                score += 1
                                break

            elif won:
                self.mate = crush

                new_mate_text = crush_text_font.render("Congrats! " + crush+" is now your mate!", 1, (0,0,0))
                screen.blit(new_mate_text, (200, 50))

                screen.blit(bachs[crush], (230, 150))

                menu_button = pygame.draw.rect(screen, (0, 0, 0), (600, 180, 150, 70))
                menu_button_text = eat_button_font.render("Menu", 1, (0, 255, 0))
                screen.blit(menu_button_text, (menu_button[0] + 15, menu_button[1] + 5))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        if menu_button.colliderect(mouse_pos):
                            return

            elif lost:
                lost_mate_text = crush_text_font.render("You didn't collect enough flowers!", 1, (0,0,0))
                single_text = crush_text_font.render("You are still single.", 1, (0,0,0))
                screen.blit(lost_mate_text, (200, 50))
                screen.blit(single_text, (280, 100))

                menu_button = pygame.draw.rect(screen, (0, 0, 0), (600, 180, 150, 70))
                menu_button_text = eat_button_font.render("Menu", 1, (0, 255, 0))
                screen.blit(menu_button_text, (menu_button[0] + 15, menu_button[1] + 5))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        if menu_button.colliderect(mouse_pos):
                            return

            pygame.display.flip()


    def see_frog(self):
        see = True
        while see:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)
            screen.fill((126, 217, 119))


            offsprings_string = ""
            for x in range(len(self.offsprings)):
                offsprings_string += self.offsprings[x]
                if not(x == len(self.offsprings) - 1):
                    offsprings_string += ", "


            info_font = pygame.font.SysFont('impact', 30)
            name_text = info_font.render("Frog's name is: "+ self.name, 1, (0,0,0))
            gender_text = info_font.render("Frog's gender is: "+ self.gender,1,(0,0,0))
            health_text = info_font.render("Frog's health is: "+ str(self.health) , 1,(0,0,0))
            mate_text = info_font.render("Frog's mate: "+self.mate,1,(0,0,0))
            offsprings_text = info_font.render("Frog's offsprings are: "+ offsprings_string, 1, (0, 0, 0))
            screen.blit(name_text, (260, 80))
            screen.blit(gender_text, (260, 130))
            screen.blit(health_text, (260, 180))
            screen.blit(mate_text, (260, 230))
            screen.blit(offsprings_text, (260, 280))

            menu_button = pygame.draw.rect(screen, (0, 0, 0), ((320, 350, 150, 70)))
            menu_text = eat_button_font.render("Menu", 1, (0,255,0))
            screen.blit(menu_text, (menu_button[0]+15, menu_button[1]+5))


            for event in pygame.event.get():
                if event.type == QUIT:
                    DB.closeDB()
                    pygame.quit()

                if event.type == MOUSEBUTTONDOWN:
                    if menu_button.colliderect(mouse_pos):
                        return

            pygame.display.flip()

    def have_offspring(self):
        intro = True
        base_color = (126, 217, 119)
        back_A_color = base_color
        back_B_color = base_color
        back_C_color = base_color
        back_D_color = base_color
        back_E_color = base_color
        back_F_color = base_color
        back_G_color = base_color
        back_H_color = base_color
        back_I_color = base_color
        back_tadpole_color =  base_color
        hover_color = (6, 186, 0)
        won = False
        baby_gender = random.choice(("girl", "boy"))
        question_one = False
        question_two = False
        question_three = False
        score = 0
        offspring = True
        while offspring:
            screen.fill((126, 217, 119))
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

            if intro:
                ready_font = pygame.font.SysFont('impact', 40)
                crush_text_font = pygame.font.SysFont('impact', 30)
                ready_text = ready_font.render("Are you ready to have a frog baby?", 1, (0, 0, 255))
                directions_text = crush_text_font.render("Take this quiz to find out!", 1, (0, 0, 0))
                screen.blit(ready_text, (145, 60))
                screen.blit(directions_text, (250, 140))

                start_quiz_button = pygame.draw.rect(screen, (0, 0, 0), (325, 250, 150, 70))
                start_quiz_font = pygame.font.SysFont('impact', 50)
                start_quiz_text = start_quiz_font.render("START", 1, (0, 255, 0))
                screen.blit(start_quiz_text, (start_quiz_button[0]+13, start_quiz_button[1]+5))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if start_quiz_button.colliderect(mouse_pos):
                            intro = False
                            question_one = True

            elif question_one:

                question_font = pygame.font.SysFont('impact', 35)
                question_one_text = question_font.render("What do frogs start off as, before they are frogs?", 1, (0, 0, 255))
                screen.blit(question_one_text, (58, 50))

                answers_font = pygame.font.SysFont('impact', 30)
                answer_A_text = answers_font.render("a.) Smaller Frogs", 1, (0,0,0))
                answer_B_text = answers_font.render("b.) Tadpoles", 1, (0,0,0))
                answer_C_text = answers_font.render("c.) Snakes", 1, (0,0,0))

                back_A = pygame.draw.rect(screen, back_A_color, answer_A_text.get_rect(x=300, y=170))
                back_B = pygame.draw.rect(screen, back_B_color, answer_B_text.get_rect(x=300, y=240))
                back_C = pygame.draw.rect(screen, back_C_color, answer_C_text.get_rect(x=300, y=310))

                screen.blit(answer_A_text, (300, 170))
                screen.blit(answer_B_text, (300, 240))
                screen.blit(answer_C_text, (300, 310))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if (answer_A_text.get_rect(x=300, y=170)).colliderect(mouse_pos) or (answer_C_text.get_rect(x=300, y=310)).colliderect(mouse_pos):
                            question_one = False
                            question_two = True
                        elif (answer_B_text.get_rect(x=300, y=240)).colliderect(mouse_pos):
                            score += 1
                            question_one = False
                            question_two = True

                    if event.type == MOUSEMOTION:
                        if (answer_A_text.get_rect(x=300, y=170)).colliderect(mouse_pos):
                            back_A_color = hover_color
                        else:
                            back_A_color = base_color

                        if (answer_B_text.get_rect(x=300, y=240)).colliderect(mouse_pos):
                            back_B_color = hover_color
                        else:
                            back_B_color = base_color

                        if (answer_C_text.get_rect(x=300, y=310)).colliderect(mouse_pos):
                            back_C_color = hover_color
                        else:
                            back_C_color = base_color



            elif question_two:

                question_two_text = question_font.render("What do frogs usually eat?", 1, (0,0,255))
                screen.blit(question_two_text, (210, 50))

                answer_D_text = answers_font.render("d.) Insects", 1, (0,0,0))
                answer_E_text = answers_font.render("e.) Grass", 1, (0,0,0))
                answer_F_text = answers_font.render("f.) Rocks", 1, (0,0,0))

                back_D = pygame.draw.rect(screen, back_D_color, (answer_D_text.get_rect(x=320, y=170)))
                back_E = pygame.draw.rect(screen, back_E_color, (answer_E_text.get_rect(x=320, y=240)))
                back_F = pygame.draw.rect(screen, back_F_color, (answer_F_text.get_rect(x=320, y=310)))


                screen.blit(answer_D_text, (320, 170))
                screen.blit(answer_E_text, (320, 240))
                screen.blit(answer_F_text, (320, 310))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEMOTION:
                        if (answer_D_text.get_rect(x=320, y=170)).colliderect(mouse_pos):
                            back_D_color = hover_color
                        else:
                            back_D_color = base_color
                        if (answer_E_text.get_rect(x=320, y=240)).colliderect(mouse_pos):
                            back_E_color = hover_color
                        else:
                            back_E_color = base_color
                        if (answer_F_text.get_rect(x=320, y=310)).colliderect(mouse_pos):
                            back_F_color = hover_color
                        else:
                            back_F_color = base_color

                    if event.type == MOUSEBUTTONDOWN:
                        if (answer_D_text.get_rect(x=320, y=170)).colliderect(mouse_pos):
                            score += 1
                            question_two = False
                            question_three = True
                        elif (answer_E_text.get_rect(x=320, y=240)).colliderect(mouse_pos) or (answer_F_text.get_rect(x=320, y=310)).colliderect(mouse_pos):
                            question_two = False
                            question_three = True

            elif question_three:
                question_three_text = question_font.render("How do frogs catch insects?", 1, (0, 0, 255))
                screen.blit(question_three_text, (210, 50))

                answer_G_text = answers_font.render("g.) With their hands", 1, (0, 0, 0))
                answer_H_text = answers_font.render("h.) With their legs", 1, (0, 0, 0))
                answer_I_text = answers_font.render("i.) With their tongue", 1, (0, 0, 0))

                back_G = pygame.draw.rect(screen, back_G_color, (answer_G_text.get_rect(x=280, y=170)))
                back_H = pygame.draw.rect(screen, back_H_color, (answer_H_text.get_rect(x=280, y=240)))
                back_I = pygame.draw.rect(screen, back_I_color, (answer_I_text.get_rect(x=280, y=310)))

                screen.blit(answer_G_text, (280, 170))
                screen.blit(answer_H_text, (280, 240))
                screen.blit(answer_I_text, (280, 310))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEMOTION:
                        if (answer_G_text.get_rect(x=280, y=170)).colliderect(mouse_pos):
                            back_G_color = hover_color
                        else:
                            back_G_color = base_color
                        if (answer_H_text.get_rect(x=280, y=240)).colliderect(mouse_pos):
                            back_H_color = hover_color
                        else:
                            back_H_color = base_color
                        if (answer_I_text.get_rect(x=280, y=310)).colliderect(mouse_pos):
                            back_I_color = hover_color
                        else:
                            back_I_color = base_color

                    if event.type == MOUSEBUTTONDOWN:
                        if (answer_I_text.get_rect(x=280, y=310)).colliderect(mouse_pos):
                            score += 1
                            if score == 3:
                                won = True
                            question_three = False
                        elif (answer_G_text.get_rect(x=280, y=170)).colliderect(mouse_pos) or \
                                (answer_H_text.get_rect(x=280, y=240)).colliderect(mouse_pos):
                            won = False
                            question_three = False



            elif won:
                fill_out = False
                congrats_font = pygame.font.SysFont('impact', 45)
                congrats_text = congrats_font.render("Congratulations!", 1, (6, 100, 0))
                baby_text = question_font.render("You now have a beautiful tadpole " + baby_gender, 1, (0, 0, 0))
                name_them_font = pygame.font.SysFont('impact', 25)
                name_them_text = name_them_font.render("(Click on your tadpole to name it)", 1, (255, 0, 0))


                screen.blit(congrats_text, (260, 50))
                screen.blit(baby_text, (140, 120))
                screen.blit(name_them_text, (240, 180))

                back_tadpole = pygame.draw.rect(screen, back_tadpole_color, tadpole.get_rect(x=120, y=230))

                screen.blit(tadpole, (120, 230))


                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()

                    if event.type == MOUSEBUTTONDOWN:
                        if (tadpole.get_rect(x=120, y=230)).colliderect(mouse_pos):
                            fill_out = True

                    if event.type == MOUSEMOTION:
                        if (tadpole.get_rect(x=120, y=230)).colliderect(mouse_pos):
                            back_tadpole_color = hover_color
                        else:
                            back_tadpole_color = base_color

                if fill_out:
                    baby_name = ""
                    textbox_activated = False
                    textbox_color = (255, 255, 255)
                    click_text_on = True
                    naming = True
                    while naming:
                        screen.fill((126, 217, 119))
                        mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

                        screen.blit(birth_certificate, (50, 15))

                        parents_names_font = pygame.font.SysFont('calibri', 35, bold=True)
                        main_parent_text = parents_names_font.render(self.name, 1, (0, 0, 0))
                        other_parent_text = parents_names_font.render(self.mate, 1, (0, 0, 0))
                        screen.blit(main_parent_text, (245, 370))
                        screen.blit(other_parent_text, (520, 370))

                        if baby_gender == "girl":
                            baby_gender_text = parents_names_font.render("Female", 1, (0, 0, 0))
                        elif baby_gender == "boy":
                            baby_gender_text = parents_names_font.render("Male", 1, (0, 0, 0))

                        screen.blit(baby_gender_text, (250, 280))

                        done_button = pygame.draw.rect(screen, (0, 0, 0), (500, 140, 150, 70))
                        done_button_font = pygame.font.SysFont('impact', 50)
                        done_button_text = done_button_font.render("DONE", 1, (0, 255, 0))
                        screen.blit(done_button_text, (done_button[0] + 23, done_button[1] + 7))


                        textbox = pygame.draw.rect(screen, textbox_color, (240, 160, 170, 50))

                        if click_text_on:
                            click_text = parents_names_font.render("Click here", 1, (255, 0, 0))
                            screen.blit(click_text, (textbox[0]+5, textbox[1]+15))

                        baby_name_font = pygame.font.SysFont('calibri', 35, bold=True)
                        baby_name_text = baby_name_font.render(baby_name, 1, (0, 0, 0))
                        screen.blit(baby_name_text, (textbox[0]+5, textbox[1]+15))

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                DB.closeDB()
                                pygame.quit()

                            if event.type == MOUSEBUTTONDOWN:
                                if done_button.colliderect(mouse_pos):
                                    self.offsprings.append(baby_name)
                                    return

                                if textbox.colliderect(mouse_pos):
                                    textbox_activated = True
                                    click_text_on = False
                                    textbox_color = (180, 255, 180)
                                else:
                                    textbox_activated = False
                                    textbox_color = (245, 238, 218)

                            if event.type == KEYDOWN:
                                if textbox_activated:
                                    if event.key == K_RETURN:
                                        textbox_activated = False
                                        textbox_color = (245, 238, 218)
                                    elif event.key == K_BACKSPACE:
                                        baby_name = baby_name[:-1]
                                    else:
                                        baby_name += event.unicode

                        pygame.display.flip()

            elif not won:

                you_lost_font = pygame.font.SysFont('juiceitc', 60)
                you_lost_text = you_lost_font.render("You didn't pass the quiz!", 1, (0, 0, 0))
                screen.blit(you_lost_text, (200, 100))

                menu_button = pygame.draw.rect(screen, (0, 0, 0), ((320, 250, 150, 70)))
                menu_text = eat_button_font.render("Menu", 1, (0, 255, 0))
                screen.blit(menu_text, (menu_button[0] + 15, menu_button[1] + 5))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        DB.closeDB()
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        if menu_button.colliderect(mouse_pos):
                            return

            pygame.display.flip()

    def save(self):
        #saves their info the db here
        offspring_string = ""
        for offspring in self.offsprings:
            offspring_string += offspring
            if offspring != self.offsprings[-1]:
                offspring_string += ", "
        DB.insert(self.name, self.gender, self.health, self.mate, offspring_string)
        save_on = True
        while save_on:
            screen.fill((126, 217, 119))
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

            saved_font = pygame.font.SysFont('impact', 30)
            saved_text = saved_font.render("Your frog data has been saved as:", 1, (0, 0, 0))
            screen.blit(saved_text, (200, 100))

            info_text1 = saved_font.render("Name: {name}, Gender: {gender}, Health: {health}".format(name=self.name, gender=self.gender, health=self.health),1, (0, 0, 0))
            screen.blit(info_text1, (180, 170))
            info_text2 = saved_font.render("Mate: {mate}, Offsprings: {offsprings}".format(mate=self.mate, offsprings=offspring_string), 1, (0, 0, 0))
            screen.blit(info_text2, (180, 240))

            menu_button = pygame.draw.rect(screen, (0, 0, 0), ((320, 350, 150, 70)))
            menu_text = eat_button_font.render("Menu", 1, (0, 255, 0))
            screen.blit(menu_text, (menu_button[0] + 15, menu_button[1] + 5))

            for event in pygame.event.get():
                if event.type == QUIT:
                    DB.closeDB()
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if menu_button.colliderect(mouse_pos):
                        return

            pygame.display.flip()

def pick_name():
    textbox_color = (250, 250, 250)
    textbox_activated = False
    name = ""
    done_button_color = (0, 0, 0)
    choosing_name = True
    while choosing_name:
        mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

        screen.fill((126, 217, 119))

        name_font = pygame.font.SysFont('juiceitc', 50)
        name_text = name_font.render("Name: " + name, 1, (0, 0, 0))
        screen.blit(name_text, name_text.get_rect(centerx=400, centery=70))

        done_button = pygame.Rect(320, 150, 150, 70)
        pygame.draw.rect(screen, done_button_color, done_button)

        done_button_font = pygame.font.SysFont('impact', 50)
        done_button_text = done_button_font.render("DONE", 1, (0, 255, 0))
        screen.blit(done_button_text, (done_button[0]+23, done_button[1]+7))

        textbox = pygame.Rect(320, 250, 150, 70)
        pygame.draw.rect(screen, textbox_color, textbox)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                DB.closeDB()
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if done_button.colliderect(mouse_pos):
                    choosing_name = False
                else:
                    if textbox.colliderect(mouse_pos):
                        textbox_activated = True
                        textbox_color = (250, 0, 0)
                    else:
                        textbox_activated = False
                        textbox_color = (250, 250, 250)

            if event.type == KEYDOWN:
                if textbox_activated:
                    if event.key == K_RETURN:
                        textbox_activated = False
                        textbox_color = (250, 250, 250)
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            if event.type == MOUSEMOTION:
                if done_button.colliderect(mouse_pos):
                    done_button_color = (6, 186, 0)
                else:
                    done_button_color = (0, 0, 0)

        textbox_font = pygame.font.Font(None, 40)
        textbox_text = textbox_font.render(name, 1, (0, 0, 0))
        screen.blit(textbox_text, textbox)


        pygame.display.flip()

    return name

def pick_gender():
    male_box_color = (126, 217, 119)
    female_box_color = (126, 217, 119)
    picking_gender = True
    while picking_gender:
        mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

        screen.fill((126, 217, 119))

        choose_gender_font = pygame.font.SysFont('juiceitc', 50)
        choose_gender_text = choose_gender_font.render("Choose Gender", 1, (0, 0, 0))
        screen.blit(choose_gender_text, choose_gender_text.get_rect(centerx=400, centery=70))

        gender_text = pygame.font.SysFont("impact", 30)
        male_frog_text = gender_text.render("Male", 1, (0, 0, 0))
        female_frog_text = gender_text.render("Female", 1, (0, 0, 0))
        screen.blit(male_frog_text, male_frog_text.get_rect(centerx=200, centery=150))
        screen.blit(female_frog_text, female_frog_text.get_rect(centerx=600, centery=150))


        male_frog_dim = male_frog.get_rect(centerx=200, centery=350)
        male_box = pygame.draw.rect(screen, male_box_color, male_frog_dim)
        screen.blit(male_frog, male_frog_dim)



        female_frog_dim = female_frog.get_rect(centerx=600, centery=350)
        female_box = pygame.draw.rect(screen, female_box_color, female_frog_dim)
        screen.blit(female_frog, female_frog_dim)


        for event in pygame.event.get():
            if event.type == QUIT:
                DB.closeDB()
                pygame.quit()
            if event.type == MOUSEMOTION:
                if male_frog_dim.colliderect(mouse_pos):
                    male_box_color = (6, 186, 0)
                else:
                    male_box_color = (126, 217, 119)

            if event.type == MOUSEBUTTONDOWN:
                if male_frog_dim.colliderect(mouse_pos):
                    gender = "male"
                    picking_gender = False
            if event.type == MOUSEMOTION:
                if female_frog_dim.colliderect(mouse_pos):
                    female_box_color = (6, 186, 0)
                else:
                    female_box_color = (126, 217, 119)

            if event.type == MOUSEBUTTONDOWN:
                if female_frog_dim.colliderect(mouse_pos):
                    gender = "female"
                    picking_gender = False

        pygame.display.flip()
    return gender





button_color = (0, 0, 0)
loadbutton_color = (0, 0, 0)
load_frog = False
already = False
no_mate = False
menu = False
while not menu and not load_frog:
    mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

    screen.fill((68, 209, 2))

    title_font = pygame.font.SysFont('juiceitc', 60)
    title = title_font.render("Welcome to Frog Simulator!", 1, (0, 0, 0))
    screen.blit(title, title.get_rect(centerx = 400, centery = 150))

    # rect = (x, y, width, height)

    button = pygame.draw.rect(screen, button_color, (220, 250, 150, 70))

    button_text_font = pygame.font.SysFont('impact', 40)
    button_text = button_text_font.render("START", 1, (0, 255, 0))
    button_text_dim = (button[0] + 27, button[1] + 12)
    screen.blit(button_text, button_text_dim)

    load_button = pygame.draw.rect(screen, loadbutton_color, (440, 250, 150, 70))
    load_font = pygame.font.SysFont('impact', 30)
    load_text = load_font.render("Load Saved", 1, (0, 255, 0))
    load_text2 = load_font.render("Frog", 1, (0, 255, 0))
    screen.blit(load_text, (load_button[0]+3, load_button[1]))
    screen.blit(load_text2, (load_button[0]+45, load_button[1]+30))

    for event in pygame.event.get():
        if event.type == QUIT:
            DB.closeDB()
            pygame.quit()
        if event.type == MOUSEMOTION:
            if button.colliderect(mouse_pos):
                button_color = (15, 148, 6)
            else:
                button_color = (0, 0, 0)
            if load_button.colliderect(mouse_pos):
                loadbutton_color = (15, 148, 6)
            else:
                loadbutton_color = (0, 0, 0)
        if event.type == MOUSEBUTTONDOWN:
            if button.colliderect(mouse_pos):
                new_frog = Frog(pick_gender(), pick_name())
                menu = True
            elif load_button.colliderect(mouse_pos):
                load_frog = True




    pygame.display.flip()

if load_frog:
    # gets all names of frogs in the DB and puts them in a list
    FrogsinDB = []
    for frog in DB.get_all_frog():
        FrogsinDB.append(frog[0])

    print(FrogsinDB)

    FrogsinDB_string = ""
    for name in FrogsinDB:
        FrogsinDB_string += name
        if name != FrogsinDB[-1]:
            FrogsinDB_string += ", "

click_here = True
textbox_color = (255, 255, 255)
textbox_activated = False
NotInSystem = False
frogname = ""
while load_frog:
    mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)
    screen.fill((68, 209, 2))
    """
    back_button = pygame.draw.rect(screen, (0, 0, 0), (70, 300, 150, 70))
    back_font = pygame.font.SysFont('impact', 50)
    back_text = back_font.render("BACK", 1, (0, 255, 0))
    screen.blit(back_text, (back_button[0]+20, back_button[1]+5))
    """

    pick_font = pygame.font.SysFont('juiceitc', 60)
    pick_text = pick_font.render("Type in which of these Frogs is yours", 1, (0, 0, 0))
    screen.blit(pick_text, (100, 50))

    names_font = pygame.font.SysFont('impact', 30)
    names_text = names_font.render("Saved Frogs: " + FrogsinDB_string, 1, (0, 0, 0))
    screen.blit(names_text, (30, 200))

    text_box = pygame.draw.rect(screen, textbox_color, (280, 300, 250, 90))

    if click_here:
        click_font = pygame.font.SysFont('impact', 45)
        click_text = click_font.render("Click here", 1, (100, 100, 255))
        screen.blit(click_text, (text_box[0], text_box[1] + 10))

    textbox_font = pygame.font.SysFont('impact', 40)
    textbox_text = textbox_font.render(frogname, 1, (0, 0, 0))
    screen.blit(textbox_text, (text_box[0], text_box[1]+20))

    done_button = pygame.draw.rect(screen, (0, 0, 0), (550, 300, 150, 70))
    done_font = pygame.font.SysFont('impact', 50)
    done_text = done_font.render("DONE", 1, (0, 255, 0))
    screen.blit(done_text, (done_button[0]+25, done_button[1]+5))

    if NotInSystem:
        system_font = pygame.font.SysFont('impact', 30)
        system_text = system_font.render("That name is not in the system!", 1, (0, 0, 0))
        screen.blit(system_text, (270, 400))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if text_box.colliderect(mouse_pos):
                textbox_activated = True
                click_here = False
                textbox_color = (255, 100, 100)
            if done_button.colliderect(mouse_pos):
                textbox_activated = False
                textbox_color = (255, 255, 255)
                new_frog_info = DB.get_frog(frogname)
                if new_frog_info is not None:
                    offspring_list = new_frog_info[4].split(", ")
                    new_frog = Frog(new_frog_info[1], new_frog_info[0], new_frog_info[2], new_frog_info[3], offspring_list)
                    load_frog = False
                    menu = True
                else:
                    NotInSystem = True

        if event.type == KEYDOWN:
            if textbox_activated:
                if event.key == K_RETURN:
                    textbox_activated = False
                    textbox_color = (255, 255, 255)
                elif event.key == K_BACKSPACE:
                    frogname = frogname[:-1]
                else:
                    frogname += event.unicode




    pygame.display.flip()


eat_button_color = (0, 0, 0)
fight_button_color = (0, 0, 0)
mate_button_color = (0, 0, 0)
see_button_color = (0, 0, 0)
offspring_button_color = (0, 0, 0)
save_button_color = (0, 0, 0)
while menu:
    mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2, 2)

    screen.fill((68, 209, 2))

    choose_action_font = pygame.font.SysFont('juiceitc', 60)
    choose_action_text = choose_action_font.render("Choose what to do!", 1, (0, 0, 0))
    screen.blit(choose_action_text, (250, 50))

    eat_button = pygame.Rect(80, 200, 150, 70)
    pygame.draw.rect(screen, eat_button_color, eat_button)
    eat_button_font = pygame.font.SysFont('impact', 50)
    eat_button_text = eat_button_font.render("Eat", 1, (0, 255, 0))
    screen.blit(eat_button_text, (eat_button[0] + 45, eat_button[1] + 5))

    fight_button = pygame.draw.rect(screen, fight_button_color, (330, 200, 150, 70))
    fight_button_text = eat_button_font.render("Fight", 1, (0, 255, 0))
    screen.blit(fight_button_text, (fight_button[0] + 25, fight_button[1] + 5))

    mate_button = pygame.draw.rect(screen, mate_button_color, (580, 200, 150, 70))
    mate_button_text = eat_button_font.render("Mate", 1, (0, 255, 0))
    screen.blit(mate_button_text, (mate_button[0]+25, mate_button[1]+5))

    see_button = pygame.draw.rect(screen, see_button_color, (80, 350, 150, 70))
    see_button_font = pygame.font.SysFont('impact', 40)
    see_button_text = see_button_font.render("See Frog", 1, (0,255,0))
    screen.blit(see_button_text, (see_button[0]+5, see_button[1]+5))

    offspring_button = pygame.draw.rect(screen, offspring_button_color, (330, 350, 150, 70))
    offspring_button_text = see_button_font.render("Offspring",1, (0, 255, 0))
    screen.blit(offspring_button_text, (offspring_button[0], offspring_button[1]+5))

    save_button = pygame.draw.rect(screen, save_button_color, (580, 350, 150, 70))
    save_button_text = eat_button_font.render("Save", 1, (0, 255, 0))
    screen.blit(save_button_text, (save_button[0]+25, save_button[1]+5))

    for event in pygame.event.get():
        if event.type == QUIT:
            DB.closeDB()
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            if eat_button.colliderect(mouse_pos):
                new_frog.eat()
            if mate_button.colliderect(mouse_pos):
                if new_frog.mate == "single":
                    new_frog.find_mate()
                else:
                    already = True
                    sec_passed = 0
                    warning_clock = pygame.time.Clock()

            if fight_button.colliderect(mouse_pos):
                if new_frog.fight() == "died":
                    DB.delete_single_row(new_frog.name)
                    new_frog = Frog(pick_gender(), pick_name())

            if see_button.colliderect(mouse_pos):
                new_frog.see_frog()

            if offspring_button.colliderect(mouse_pos):
                if new_frog.mate != "single":
                    new_frog.have_offspring()
                else:
                    no_mate = True
                    nomate_sec_passed = 0
                    nomate_clock = pygame.time.Clock()
            if save_button.colliderect(mouse_pos):
                new_frog.save()


        if event.type == MOUSEMOTION:
            if eat_button.colliderect(mouse_pos):
                eat_button_color = (6, 186, 0)
            else:
                eat_button_color = (0, 0, 0)
            if mate_button.colliderect(mouse_pos):
                mate_button_color = (6, 186, 0)
            else:
                mate_button_color = (0, 0, 0)
            if fight_button.colliderect(mouse_pos):
                fight_button_color = (6, 186, 0)
            else:
                fight_button_color = (0, 0, 0)

            if see_button.colliderect(mouse_pos):
                see_button_color = (6, 186, 0)
            else:
                see_button_color = (0, 0, 0)

            if offspring_button.colliderect(mouse_pos):
                offspring_button_color = (6, 186, 0)
            else:
                offspring_button_color = (0, 0, 0)

            if save_button.colliderect(mouse_pos):
                save_button_color = (6, 186, 0)
            else:
                save_button_color = (0, 0, 0)
    if already:
        already_text_font = pygame.font.SysFont('impact', 30)
        already_text = already_text_font.render("You already have a mate!", 1, (0, 0, 0))
        screen.blit(already_text, (250, 300))
        sec_passed += warning_clock.tick()
        if sec_passed > 6000:
            already = False
    if no_mate:
        no_mate_font = pygame.font.SysFont('impact', 30)
        no_mate_text = no_mate_font.render("You need a mate first!", 1, (0, 0, 0))
        screen.blit(no_mate_text, (280, 300))
        nomate_sec_passed += nomate_clock.tick()
        if nomate_sec_passed > 6000:
            no_mate = False



    pygame.display.flip()
