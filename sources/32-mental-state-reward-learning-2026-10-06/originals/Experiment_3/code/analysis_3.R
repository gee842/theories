####################Data analysis script for Experiment 2#######################
#Authors: Yi Zhang, Leor Hackel
#May 2024

#clear environment
rm(list = ls())

#set path to the project folder
path <- getwd()

####################Main Analyses: Optimal Choice####################
#load required packages
library(tidyverse) #for cleaning data
library(lme4) #for running mixed-effect models
library(lmerTest) #for calculating p-value for mixed-effect models
library(emmeans) #for simple effects

#read data
data_dm <- read.csv(paste0(path, "/Experiment_3/data_clean/data_3.csv"), header = TRUE)

#remove reaction times <= 200ms
data_dm_original <- data_dm
data_dm <- data_dm%>%filter(DM_choice_component.rt >= 0.2)

#Does contingency reversal influence probability of optimal choice?
#Good feelings as a function of congruence and outcome type
#(Main manuscript: Page 37)
m.reversal <- glmer(factor(optimal) ~ 
                              condition_change_recode +
                              (1 | ID_anonymous),
                            family = "binomial",
                            data = data_dm)
summary(m.reversal) #not significant
#compute 95% CI
confint.merMod(m.reversal, method = "Wald")

#keeping outliers (based pre-registration)
m.reversal <- glmer(factor(optimal) ~ 
                      condition_change_recode +
                      (1 | ID_anonymous),
                    family = "binomial",
                    data = data_dm_original)
summary(m.reversal) #not significant
#compute 95% CI
confint.merMod(m.reversal, method = "Wald")


####################Secondary Analyses: Moderation by Contingency Awareness on Optimal Choice####################
#Does the impact of contingency reversal on optimal choice depend on contingency
#awareness?
#(Main manuscript: Page 37; Supplement: P27)
m.reversal.aware <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            contingency_awareness_1_recode+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.aware) #significant
#compute 95% CI
confint.merMod(m.reversal.aware, method = "Wald")

#simple effects
#(Main manuscript: Page 37-38)
em_means <- emmeans(m.reversal.aware, ~ condition_change_recode 
                    | contingency_awareness_1_recode)
contrast <- contrast(em_means, "revpairwise")
# View estimated marginal means or predicted probabilities
print(contrast)


#keeping outliers (based pre-registration)
#(Supplement: P27)
m.reversal.aware <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            contingency_awareness_1_recode+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm_original)
summary(m.reversal.aware) #significant
#compute 95% CI
confint.merMod(m.reversal.aware, method = "Wald")


####################Secondary Analyses: Reaction Time####################
#Does contingency reversal impact reaction time during the decision-making phase?
#(Main manuscript: P38; Supplement: P28)
m.reversal.rt <- lmer(log(DM_choice_component.rt) ~ 
                            condition_change_recode+
                            (1 | ID_anonymous),
                          data = data_dm)
summary(m.reversal.rt) #significant
#compute 95% CI
confint.merMod(m.reversal.rt, method = "Wald")

#keeping outliers
#(Supplement: P28)
m.reversal.rt <- lmer(log(DM_choice_component.rt) ~ 
                        condition_change_recode +
                        (1 | ID_anonymous),
                      #remove reaction time = 0
                      data = data_dm_original%>%filter(DM_choice_component.rt>0))
summary(m.reversal.rt) #marginally significant
#compute 95% CI
confint.merMod(m.reversal.rt, method = "Wald")

#using un-transformed RT as the DV
m.reversal.rt <- lmer(DM_choice_component.rt ~ 
                        condition_change_recode +
                        (1 | ID_anonymous),
                      #remove reaction time = 0
                      data = data_dm_original%>%filter(DM_choice_component.rt>0))
summary(m.reversal.rt) #marginally significant
#compute 95% CI
confint.merMod(m.reversal.rt, method = "Wald")


####################Secondary Analyses: Moderation by Contingency Awareness on RT####################
#removing outliers (<200ms)
m.reversal.rt <- lmer(log(DM_choice_component.rt) ~ 
                        condition_change_recode * contingency_awareness_1_recode +
                        (1 | ID_anonymous),
                      #remove reaction time = 0
                      data = data_dm%>%filter(DM_choice_component.rt > 0))
summary(m.reversal.rt) #non-significant
#compute 95% CI
confint.merMod(m.reversal.rt, method = "Wald")

#based on pre-registration (keeping outliers)
#(Supplement: P28)
m.reversal.rt <- lmer(log(DM_choice_component.rt) ~ 
                        condition_change_recode * contingency_awareness_1_recode+
                        (1 | ID_anonymous),
                      #remove reaction time = 0
                      data = data_dm_original%>%filter(DM_choice_component.rt>0))
summary(m.reversal.rt) #non-significant
#compute 95% CI
confint.merMod(m.reversal.rt, method = "Wald")


####################Secondary Analyses: Other Moderation Effects####################
#Contingency perception accuracy (continuous) as moderator
#(Supplement: P36)
m.reversal.aware <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            perceive_contingent.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.aware) #significant
#compute 95% CI
confint.merMod(m.reversal.aware, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.aware <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            perceive_contingent.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm_original)
summary(m.reversal.aware) #significant
#compute 95% CI
confint.merMod(m.reversal.aware, method = "Wald")


#Trait Empathy (Empathic Concern) as moderator
#(Supplement: P36)
m.reversal.iri_ec <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            iri_ec.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.iri_ec) #not significant
#compute 95% CI
confint.merMod(m.reversal.iri_ec, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.iri_ec <- glmer(factor(optimal) ~ 
                             condition_change_recode *
                             iri_ec.c+
                             (1 | ID_anonymous),
                           family = "binomial",
                           data = data_dm_original)
summary(m.reversal.iri_ec) #not significant
#compute 95% CI
confint.merMod(m.reversal.iri_ec, method = "Wald")


#Trait Empathy (Perspective-Taking) as moderator
#(Supplement: P36)
m.reversal.iri_pt <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            iri_pt.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.iri_pt) #not significant
#compute 95% CI
confint.merMod(m.reversal.iri_pt, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.iri_pt <- glmer(factor(optimal) ~ 
                             condition_change_recode *
                             iri_pt.c+
                             (1 | ID_anonymous),
                           family = "binomial",
                           data = data_dm_original)
summary(m.reversal.iri_pt) #not significant
#compute 95% CI
confint.merMod(m.reversal.iri_pt, method = "Wald")


#Liking of target (pleasantness) as moderator
#(Supplement: P36)
m.reversal.pleasant <- glmer(factor(optimal) ~ 
                               condition_change_recode *
                               pleasantness.c+
                               (1 | ID_anonymous),
                             family = "binomial",
                             data = data_dm)
summary(m.reversal.pleasant) #not significant
#compute 95% CI
confint.merMod(m.reversal.pleasant, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.pleasant <- glmer(factor(optimal) ~ 
                               condition_change_recode *
                               pleasantness.c+
                               (1 | ID_anonymous),
                             family = "binomial",
                             data = data_dm_original)
summary(m.reversal.pleasant) #not significant
#compute 95% CI
confint.merMod(m.reversal.pleasant, method = "Wald")


#Self-reported perspective-taking during conditioning as moderator
#(Supplement: P36)
m.reversal.pt_sr <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            perspective_taking1.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.pt_sr) #significant
#compute 95% CI
confint.merMod(m.reversal.pt_sr, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.pt_sr <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            perspective_taking1.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm_original)
summary(m.reversal.pt_sr) #significant
#compute 95% CI
confint.merMod(m.reversal.pt_sr, method = "Wald")


#Image relatability as moderator
#(Supplement: P36)
m.reversal.relatable <- glmer(factor(optimal) ~ 
                            condition_change_recode *
                            relatable.c+
                            (1 | ID_anonymous),
                          family = "binomial",
                          data = data_dm)
summary(m.reversal.relatable) #not significant
#compute 95% CI
confint.merMod(m.reversal.relatable, method = "Wald")

#keeping outliers (based pre-registration)
#(Supplement: P36)
m.reversal.relatable <- glmer(factor(optimal) ~ 
                                condition_change_recode *
                                relatable.c+
                                (1 | ID_anonymous),
                              family = "binomial",
                              data = data_dm_original)
summary(m.reversal.relatable) #not significant
#compute 95% CI
confint.merMod(m.reversal.relatable, method = "Wald")


####################Secondary Analyses: Full 2*2 Design####################
#Predicting optimal choice using 1) congruence of conditioning and 2) contingency during
#prosocial decision-making
m.2_by_2 <- glmer(factor(optimal) ~ 
                    condition_recode * condition_dm_recode +
                    (1 | ID_anonymous),
                  family = "binomial",
                  data = data_dm)
summary(m.2_by_2) #interaction not significant
#compute 95% CI
confint.merMod(m.2_by_2, method = "Wald")


####################Additional analyses##########################
#Predicting prosocial choice using trait empathy (empathic concern, perspective-taking)
#create prosocial choice variable based on condition
#(Supplement: P18)
data_dm <- data_dm%>%
  mutate(prosocial = ifelse(condition_dm_recode==-1, 1-optimal, 
                            ifelse(condition_dm_recode==1, optimal, NA)))

m.prosocial.iri_ec <- glmer(factor(prosocial) ~
                              iri_ec.c+
                             (1 | ID_anonymous),
                           family = "binomial",
                           data = data_dm)
summary(m.prosocial.iri_ec) #significant
#compute 95% CI
confint.merMod(m.prosocial.iri_ec, method = "Wald")

m.prosocial.iri_pt <- glmer(factor(prosocial) ~ 
                              iri_pt.c+
                              (1 | ID_anonymous),
                            family = "binomial",
                            data = data_dm)
summary(m.prosocial.iri_pt) #not significant
#compute 95% CI
confint.merMod(m.prosocial.iri_pt, method = "Wald")

