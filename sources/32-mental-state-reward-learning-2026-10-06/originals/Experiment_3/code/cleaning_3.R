####################Data cleaning script for Experiment 3#######################
#Authors: Yi Zhang, Leor Hackel
#May 2025

#clear environment
rm(list = ls())

#set path to the project folder
path <- getwd()

#load required packages
library(tidyverse) #for cleaning data
library(psych)

##########################Import Qualtrics Raw Data#########################
post_task_survey_raw <-
  read.csv(paste0(path, "/Experiment_3/data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv"), 
           header = TRUE, stringsAsFactors = FALSE)%>%
  select(Connect.ID, EndDate, Progress, Duration..in.seconds.,
         X2_perspective_taking:attention_check
  )%>%
  filter(Progress==100)
colnames(post_task_survey_raw)[1] <- 'PID'
#The raw post-task survey contains 495 rows of data. Among these, 
#the first 106 rows (P1 - P108) were data collected as part of a pilot study
#that used the same post-task Qualtrics survey as Experiment 3.
#Data collection for Experiment 3 began on Dec-5, 2023, as stated in 
#the manuscript. Therefore, below we remove pilot data by filtering by completion date.

#remove subjects from an earlier pilot study (before Dec-5, 2023)
#recode date column so that it can be re-ordered
post_task_survey_raw$EndDate <- 
  as.POSIXct(post_task_survey_raw$EndDate, format = "%m/%d/%y %H:%M")

post_task_survey_raw <- 
  post_task_survey_raw%>%
  arrange(EndDate)%>%
  #recode attention check question (for later use)
  mutate(attention_check_recode = 
           as.numeric(as.character(substr(attention_check,1,1))))%>%
  #remove data collected before Dec-5
  filter(EndDate >= as.POSIXct("12/05/23 00:00", format = "%m/%d/%y %H:%M"))
#390 participants completed the post-task survey.
#5 responses did not have PID due to Pavlovia error. 
#Therefore, the total # of complete responses should be 385 (see below).

post_task_survey_raw <- 
  post_task_survey_raw%>%
  filter(startsWith(PID, "P"))


#Recode IRI scores
post_task_survey_iri <- post_task_survey_raw%>%
  select(PID, starts_with('IRI'))

#converting recoded response to numbers before coding
post_task_survey_iri[, 2:29] <- apply(post_task_survey_iri[2:29], 2, function(x) as.numeric(as.character(substring(x, 1, 1))))

#coding IRI (after dealing with reversely coded variables)
post_task_survey_iri[, c('IRI_3', 'IRI_4', 'IRI_7', 'IRI_12',
                         'IRI_13', 'IRI_14', 'IRI_15', 
                         'IRI_18', 'IRI_19')] <-
  apply(post_task_survey_iri[, c('IRI_3', 'IRI_4', 'IRI_7',
                                 'IRI_12','IRI_13', 'IRI_14',
                                 'IRI_15', 'IRI_18', 'IRI_19')],
        2, function(x) 6-as.numeric(x))

post_task_survey_iri <- post_task_survey_iri%>%
  mutate(iri_pt = 
           rowMeans(subset(post_task_survey_iri, 
                           select = c(IRI_3, IRI_8, IRI_11, IRI_15, 
                                      IRI_21, IRI_25, IRI_28)), na.rm = TRUE),
         iri_ec = 
           rowMeans(subset(post_task_survey_iri, 
                           select = c(IRI_2, IRI_4, IRI_9, IRI_14, 
                                      IRI_18, IRI_20, IRI_22)), na.rm = TRUE),
         iri_pd = 
           rowMeans(subset(post_task_survey_iri, 
                           select = c(IRI_6, IRI_10, IRI_13, IRI_17,
                                      IRI_19, IRI_24, IRI_27)), na.rm = TRUE))

#########################Import Pavlovia Raw Data############################
#Finding all the relevant filenames
data_dir <- paste0(path,"/Experiment_3/data_raw_primary/Pavlovia/")
file_names <-dir(data_dir, pattern =".*.csv")
#Looping through all participants 
data_condition <- data.frame()
for (name in file_names){
  temp_data <- read.csv(paste0(data_dir, name), 
                        header = TRUE,stringsAsFactors = FALSE)%>%
    select(Connect.ID,
           experimental_condition,
           condition_DM)%>%
    head(1)
  colnames(temp_data) <- c('PID', 'condition', 'condition_dm')
  data_condition <- rbind(data_condition, temp_data)
}

#Examine N for each condition
#recode condition value
data_condition <- data_condition%>%
  filter(!is.na(PID))%>%
  mutate(condition = dplyr::recode(condition, 
                                   "A" = "congruent", "B" = "incongruent"),
         condition_dm = dplyr::recode(condition_dm,
                                      "C" = "congruent", "D" = "incongruent"))

#import data from the Pavlovian learning phase
#Extract Information from the Pavlovian learning task
file_names <-dir(data_dir, pattern =".*.csv")
data_combined_learning <- data.frame()
for (name in file_names){
  temp_data <- read.csv(paste0(data_dir, name), header = TRUE,
                        stringsAsFactors = FALSE)%>%
    select(Connect.ID,
           pav_trials.thisN,
           acknowledge_resp.rt,
           TargetOutcome, Congruent
    )
  colnames(temp_data)[1] <- 'PID'
  data_combined_learning <- rbind(data_combined_learning, temp_data)
}

#removing empty rows
data_combined_learning<-
  data_combined_learning[!(data_combined_learning$Congruent ==""),]
row.names(data_combined_learning) <- NULL

#exclude NAs and those who did not complete post-task survey
data_combined_learning <- data_combined_learning%>%
  filter(!is.na(PID))%>%
  filter(PID %in% post_task_survey_raw$PID)

#Recoding Decision-Making Phase Data
data_DM <- data.frame()
for (name in file_names){
  temp_data <- read.csv(paste0(data_dir, name), header = TRUE,
                        stringsAsFactors = FALSE)
  if (!("DM_choice_component.rt"%in%colnames(temp_data))){
    next
  }
  temp_data <- temp_data%>%
    select(Connect.ID,
           n_trial, 
           left_pic, right_pic,
           outcome_dm, dm_state, 
           DM_choice_component.keys, DM_choice_component.rt
    )
  colnames(temp_data)[1] <- 'PID'
  data_DM <- rbind(data_DM, temp_data)
}

#remove empty rows
data_DM <- data_DM[!is.na(data_DM$n_trial), ]

#add condition file
data_DM_combined <- left_join(data_condition, data_DM,
                              by = 'PID')

#add chosen information
data_DM_combined <- data_DM_combined%>%
  mutate(chosen = ifelse(DM_choice_component.keys=="e", substr(left_pic, 10, 12),
                         ifelse(DM_choice_component.keys=="i",
                                substr(right_pic, 10, 12),
                                NA)))

#recode to add optimal information
data_DM_combined <- data_DM_combined%>%
  mutate(optimal = 
           ifelse(((condition_dm == "congruent")&(chosen == "lik")),
                  1, ifelse(((condition_dm == "incongruent")&(chosen == "dis")),
                            1,
                            ifelse(((condition_dm == "congruent")&(chosen == "dis")),
                                   0, 
                                   ifelse(((condition_dm == "incongruent")&(chosen == "lik")),
                                          0, 
                                          NA)
                            )
                  )
           )
  )

#recode to add prosocial information
data_DM_combined <- data_DM_combined%>%
  mutate(prosocial = 
           ifelse(chosen == "lik", 1,
                  ifelse(chosen == "dis", 0, NA)))

#recode to add reversal information
data_DM_combined <- data_DM_combined%>%
  mutate(condition_change = 
           ifelse(condition == condition_dm, "no_change", "change"))

#Code pleasantness rating
data_combined_liking <- data.frame()
for (name in file_names){
    temp_data <- read.csv(paste0(data_dir, name), header = TRUE,
                          stringsAsFactors = FALSE)%>%
      select(Connect.ID,
             slider_pleasant.response)
    colnames(temp_data) <- c('PID', 'pleasantness')
    data_combined_liking <- rbind(data_combined_liking, temp_data)
}
#removing empty rows
data_combined_liking<-
  data_combined_liking[!(is.na(data_combined_liking$pleasantness)),]
data_combined_liking<-
  data_combined_liking[!(is.na(data_combined_liking$PID)),]
row.names(data_combined_liking) <- NULL

#Add condition column to the df
data_combined_liking <- left_join(data_condition, data_combined_liking,
                                  by = 'PID')

#Clean decision-making phase data
#remove NA trials
data_DM_combined <- data_DM_combined%>%
  filter(!is.na(DM_choice_component.rt))

#recode condition to -1 (incongruent) and 1 (congruent)
data_DM_combined <- data_DM_combined%>%
  mutate(condition_recode = 
           dplyr::recode(condition, "congruent" = 1, "incongruent" = -1),
         condition_dm_recode = 
           dplyr::recode(condition_dm, "congruent" = 1, "incongruent" = -1),
         condition_change_recode = 
           dplyr::recode(condition_change, "change" = 1, "no_change" = -1))


#import other post-task measures
#We measured three task perception variables:
# - participants' preference for a list of restaurants (which they later saw in the empathy and PIT phases)
# - `similarity`: How similar is the other person's restaurant preferences to your own?
# - `perspective_taking`: "To what extent did you consider the other person's thoughts and feelings?" (1: Not at all - 5: Very Much)
# - `outcome_relationship`: Did you notice any relationship between the other person's events and your stock outcome?
#- `perceive_contingent1`: "When the other person's stock goes **up**, how likely is it that your stock also goes up?" (1: Very unlikely - 5: Very likely)
#- `perceive_contingent2`: "When the other person's stock goes **down**, how likely is it that your stock also goes down?" (1: Very unlikely - 5: Very likely)
#- The average of the two conitngency awareness measures reflect the extent to which participants saw the other person's outcomes as consistent with their own outcomes. The average value can then be recoded to reflect participants' awareness of the contingency.

post_task_survey_task_perception <- post_task_survey_raw%>%
  select(PID,
         starts_with("X2"),
         Age, Gender)

#converting recoded response to numbers before coding
post_task_survey_task_perception[, c(2,3,6,7,8,11,12)] <- 
  apply(post_task_survey_task_perception[, c(2,3,6,7,8,11,12)], 2, function(x) as.numeric(as.character(substring(x, 1, 1))))

#convert age to numeric
post_task_survey_task_perception$Age <- 
  as.numeric(as.character(post_task_survey_task_perception$Age))


#Data summary:
#The raw data contained 387 Pavlovia responses 
#(385 of whom also completed the post-task survey)
#This matches the 385 complete responses from the post-task survey,
#The final N of people who completed both the Pavlovia task and the post-task
#survey was 385

#people who completed the post-task survey but had no pavlovia response
setdiff(post_task_survey_raw$PID, data_condition$PID) #no one in this category


#############################Determine Excluded Participants###########################
#Identifying subjects who missed 20% or more of the trials during the learning phase of the study.
subj_to_include_pav <- data_combined_learning%>%
  group_by(PID)%>%
  dplyr::summarise(miss = sum(is.na(acknowledge_resp.rt)))%>%
  filter(miss < 8)
#349 people

#Identifying subjects who missed 20% or more of the decision-making trials
subj_to_include_dm <- data_DM%>%
  group_by(PID)%>%
  dplyr::summarise(miss = sum(is.na(DM_choice_component.rt)))%>%
  filter(miss < 7)
#379 people

#based on post-task qualtrics survey
subj_to_include_qualtrics <- post_task_survey_raw%>%
  filter(attention_check_recode < 4)%>%
  select(PID) #364 people

#find overlap between two data frames
subj_to_include <- intersect(subj_to_include_pav$PID, subj_to_include_dm$PID)
subj_to_include <- intersect(subj_to_include, subj_to_include_qualtrics$PID)
#(333 people)


############################Combining Qualtrics & Pavlovia Data########################
#mean-center variables
post_task_survey_task_perception <- post_task_survey_task_perception%>%
  filter(PID %in% subj_to_include)%>%
  mutate(perspective_taking1.c = X2_perspective_taking - 
           mean(X2_perspective_taking, na.rm = TRUE),
         perspective_taking2.c = X2_perspective_taking_2 - 
           mean(X2_perspective_taking_2, na.rm = TRUE),
         relatable.c = X2_relatable - 
           mean(X2_relatable, na.rm = TRUE),
         perceive_contingent1_1.c = X2_perceive_contingent1 - 
           mean(X2_perceive_contingent1, na.rm = TRUE),
         perceive_contingent1_2.c = X2_perceive_contingent2 - 
           mean(X2_perceive_contingent2, na.rm = TRUE),
         perceive_contingent2_1.c = X2_perceive_cont_2_1 - 
           mean(X2_perceive_cont_2_1, na.rm = TRUE),
         perceive_contingent2_2.c = X2_perceive_cont_2_2 - 
           mean(X2_perceive_cont_2_2, na.rm = TRUE),
         age.c = Age - mean(Age, na.rm = TRUE)
  )

#mean-center empathy scores
data_iri <- post_task_survey_iri%>%
  filter(PID %in% subj_to_include)%>%
  mutate(iri_pt.c = iri_pt - mean(iri_pt, na.rm = TRUE),
         iri_ec.c = iri_ec - mean(iri_ec, na.rm = TRUE),
         iri_pd.c = iri_pd - mean(iri_pd, na.rm = TRUE))

#mean-center pleasantness
data_pleasant <- data_combined_liking%>%
  filter(PID %in% subj_to_include)%>%
  mutate(pleasantness.c = pleasantness - mean(pleasantness, na.rm = TRUE))

#add variables to original data set
data_DM_moderators <- data_DM_combined

#remove unqualified participants
data_DM_moderators <- data_DM_combined%>%
  filter(PID %in% subj_to_include)

data_DM_moderators <- left_join(data_DM_moderators,
                                post_task_survey_task_perception
                                [, c(1,4,6,7,9, 13:22)],
                                by = 'PID')

#recode contingency awareness
#the first measure is for the conditioning phase
#the second measure is for the decision-making phase
data_DM_moderators <- data_DM_moderators%>%
  mutate(contingency_awareness_1 = 
           ifelse(startsWith(X2_outcome_relationship, "No"), "No", 
                  ifelse(startsWith(X2_outcome_relationship, "Yes"), "Yes", NA)),
         contingency_awareness_2 = 
           ifelse(startsWith(X2_outcome_relation_2, "No"), "No", 
                  ifelse(startsWith(X2_outcome_relation_2, "Yes"), "Yes", NA))
  )

data_DM_moderators <- data_DM_moderators%>%
  mutate(perceive_contingent = 
           (ifelse(condition=="congruent",
                   X2_perceive_contingent1 - X2_perceive_contingent2,
                   ifelse(condition == "incongruent",
                          X2_perceive_contingent2 - X2_perceive_contingent1,
                          NA))
           )
  )%>%
  mutate(perceive_contingent.c = perceive_contingent - 
           mean(perceive_contingent, na.rm = TRUE))

#recode contingency awareness
data_DM_moderators <- data_DM_moderators%>%
  mutate(contingency_awareness_1_recode = 
           dplyr::recode(contingency_awareness_1,
                         "No" = -1, "Yes" = 1))

#add empathy (IRI)
data_DM_moderators <- left_join(data_DM_moderators, 
                                data_iri[, c(1, 33:35)],
                                by = 'PID')

#add pleasantness
data_DM_moderators <- 
  left_join(data_DM_moderators, data_pleasant[, c(1,2,3,5)],
            by = c("PID", "condition", "condition_dm"))


###########################Summarize descriptive information###########################
#filter out excluded participants from post-task survey
data_descriptive <- 
  read.csv(paste0(path, "/Experiment_3/data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv"), 
           header = TRUE, stringsAsFactors = FALSE)%>%
  filter(Status == "IP Address" & Progress == 100 & startsWith(Connect.ID, "P"))%>%
  select(Connect.ID, Age, Gender)%>%
  mutate(Age = as.numeric(as.character(Age)))%>%
  filter(Connect.ID %in% subj_to_include)

#age distribution
summary(data_descriptive$Age)
sd(data_descriptive$Age)

#gender distribution
table(data_descriptive$Gender)


###########################Export Cleaned CSV Files###########################
data_export_dm <- data_DM_moderators%>%
  select(PID, condition_recode, condition_dm_recode, condition_change_recode,
         n_trial, optimal, DM_choice_component.rt,
         contingency_awareness_1_recode, perceive_contingent.c,
         iri_pt.c, iri_ec.c, iri_pd.c,
         perspective_taking1.c, relatable.c, pleasantness.c)

#anonymize ids
# Step 1: Create a mapping from unique IDs to numbers
unique_ids <- unique(data_export_dm$PID)
id_mapping <- setNames(seq_along(unique_ids), unique_ids)

# Step 2: Replace the IDs in the data frame using this mapping
data_export_dm$ID_anonymous <- id_mapping[data_export_dm$PID]

data_export_dm <- 
  data_export_dm%>%
  select(ID_anonymous, condition_recode:pleasantness.c
  )

#write csv file
#(may need to adjust saved file directory accordingly)
write.csv(data_export_dm, file = paste0(path, "/Experiment_3/data_clean/data_3.csv"))

