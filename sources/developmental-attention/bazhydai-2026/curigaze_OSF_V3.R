# Data wrangling & exclusion ---------------------------------------------------
## Load packages ---------------------------------------------------------------
library(tidyverse) # tidy data
library(eyetrackingR) # eye tracking data analysis 
library(ggplot2) # plotting 
library(zoo) # interpolation

## import data (note your path will differ) ------------------------------------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))


# Loop to integrate data -------------------------------------------------------
### INPUT number of files to process ###
start_file <- 1
end_file <- 96

# create empty dataframe for interpolation info
interpolation_info <-
  data.frame(
    subject = numeric(0),
    condition = character(0),
    Validity  = character(0),
    left_n_Trials   = numeric(0),
    left_perc  = numeric(0),
    right_n_Trials  = numeric(0),
    right_perc  = numeric(0)
  )

## create empty dataframe for tracking who learned what
LearnedLabels <- data.frame(
  subject = numeric(0),
  condition = character(0),
  LearningTrialsN = numeric(0), # number of learning trials completed
  uniqueLearnedN = numeric(0), # number of unique novel items triggered
  LearnedFiffin = character(0),
  LearnedPizer = character(0),
  LearnedTeebu = character(0),
  LearnedVirdex = character(0),
  MeanGazeValidity = numeric(0)
)

combined_LearningBreadth <- data.frame() # set up empty dataframe for LearningBreadth

combined_trackloss <- data.frame() #set up empty dataframe for trackloss
combined_testdf <- data.frame() #set up empty dataframe for full df of the Test Phase
# i <- 999 # manual setting i
for (i in start_file:end_file) {
  if (i == 91) {
    # Skip to the next iteration if participant ID is 91 (accidentally overwrote data)
    next
  }
  print(i)
  #establish file path
  file_path <- paste0("./Data/CuriGaze_LatestData/TIDY_", i, "_gaze.txt")
  df <- read.csv(file_path, fileEncoding = "UTF-8")
  
  # replace "Subject" column with index "i", as some of the raw datafiles had
  # "999" as Subject/participant number, but the correct participant number in
  # the filename (which means a correct "i")
  df <- df %>% mutate(Subject = i)
  
  # INDEXING & FILLING SKIPPED GAZE SAMPLES + INTERPOLATION  ###################
  
  # mutate time-lag column
  df <- df %>% mutate(TimeStamp_lag = TimeStamp - lag(TimeStamp), TimeStamp)
  df <- df[-1, ] # delete first row with no time-lag indicator
  
  # mutate column of time lag to closest integer denominator of 1/1200 intervals
  # (i.e., number of continuous "perfect" samples from previous to current
  # timestamp; 1 "perfect" sample = 1000000/1200 microseconds)
  df <- df %>% mutate(int_samples = round(TimeStamp_lag/(1000000/1200)))
  
  
  # mutate column of the true cumulative sample count at each row, & another column noting and checking the raw (before filling or interpolation) gaze validity
  df <- df %>% mutate(cumulative_samples = cumsum(int_samples),
                      leftGazeValidity_check = case_when(
                        leftGazeValidity == 0 ~ "raw0",
                        leftGazeValidity == 1 ~ "raw1"
                      ),
                      rightGazeValidity_check = case_when(
                        rightGazeValidity == 0 ~ "raw0",
                        rightGazeValidity == 1 ~ "raw1"
                      )
  )
  
  # create new rows to fill in skipped timestamps, such that we get a continuous sample for interpolation 
  df_complete <- df %>% 
    complete(cumulative_samples = seq(min(cumulative_samples), max(cumulative_samples)), # index cumulative samples
             fill = list(leftX=NaN, leftY=NaN, leftGazeValidity=0, # specify that all newly filled rows should have NULL gaze info
                         rightX=NaN, rightY=NaN, rightGazeValidity=0, 
                         pupilLeftDia=NaN, pupilLeftValidity=0, pupilRightDia=NaN, pupilRightValidity=0,
                         leftGazeValidity_check="filled0", rightGazeValidity_check="filled0"), # specify which rows were newly created
             explicit = FALSE)
  
  # reorder "cumulative_samples" column to back of df (so as not to mess up the later column selections)
  df_complete <- df_complete %>% select(-cumulative_samples, cumulative_samples)
  
  
  # fill newly-filled NA rows
  df_filled <- df_complete %>%
    arrange(cumulative_samples) %>%
    fill(everything() & -any_of(c("TimeStamp", "leftX", "leftY", "rightX", "rightY", "pupilLeftDia", "pupilRightDia")), .direction = "down") # specify that NA eye-tracking data should not be filled
  
  
  # max gap for interpolation is 1.667ms:
  # (2[ms]*1000[microseconds])/(1000000[microseconds]/1200[hz]) = 2 rows
  # interpolate left-eye data
  df_interpolated <- df_filled %>% mutate(across(c(leftX, leftY), na.approx, maxgap = 2, na.rm = FALSE)) 
  # interpolate right-eye data
  df_interpolated <- df_interpolated %>% mutate(across(c(rightX, rightY), na.approx, maxgap = 2, na.rm = FALSE)) 
  
  
  # update check columns to identify successfully interpolated rows (with valid eye-tracking data)
  df_interpolated <- df_interpolated %>% mutate(
    leftGazeValidity_check = case_when(!is.na(leftX) & !is.na(leftY) & leftGazeValidity_check != "raw1" ~ "interpolated1", TRUE ~ leftGazeValidity_check),
    rightGazeValidity_check = case_when(!is.na(rightX) & !is.na(rightY) & rightGazeValidity_check != "raw1"  ~ "interpolated1", TRUE ~ rightGazeValidity_check),
    
    leftGazeValidity = case_when(leftGazeValidity_check == "interpolated1" ~ 1, TRUE ~ leftGazeValidity),
    rightGazeValidity = case_when(rightGazeValidity_check == "interpolated1" ~ 1, TRUE ~ rightGazeValidity),
  )
  
  
  left_interp_summary <- df_interpolated %>% group_by(Subject, condition, leftGazeValidity_check) %>% summarize(left_n_Trials = n()) %>% 
    mutate(left_perc = left_n_Trials/sum(left_n_Trials)*100) %>% rename(Validity = leftGazeValidity_check)
  
  right_interp_summary <- df_interpolated %>% group_by(Subject, condition, rightGazeValidity_check) %>% summarize(right_n_Trials = n()) %>% 
    mutate(right_perc = right_n_Trials/sum(right_n_Trials)*100) %>% rename(Validity = rightGazeValidity_check)
  
  
  interp_summary_merged <- merge(left_interp_summary, right_interp_summary, all.x = T, all.y = T)
  
  interpolation_info <- rbind(interpolation_info, interp_summary_merged)
  
  
  df <- df_interpolated # overwrite df and pass onto the rest of the loop
  
  
  
  
  # LEARNING PHASE PROCESSING ############################################################################################################################################
  
  
  #filter out samples for NONE and TestDuck in UttrCol (i.e., only include trials where one of the toys were displayed; warm-up phase should have been simultaneously filtered out)
  learning_df <- filter(df, UttrCol != "NONE" & UttrCol != "TestDuck")
  
  #create column for binary y/n GazeValidity from either L/R eyes
  learning_df$GazeValidity <- ifelse(learning_df$leftGazeValidity == 1 | learning_df$rightGazeValidity == 1, 1, 0) 
  
  #average out combined GazeValidity for % of valid trials 
  MeanGazeValidity <- mean(learning_df$GazeValidity)
  
  #subset only Learning phase to check for labels learned
  learning_df <- subset(learning_df, is_test == 0)
  
  # Check if the data contains each label (i.e., whether pt learned it)
  LearnedFiffin <- ifelse("Fiffin" %in% learning_df$UttrCol, "Fiffin", NA)
  LearnedPizer <- ifelse("Pizer" %in% learning_df$UttrCol, "Pizer", NA)
  LearnedTeebu <- ifelse("Teebu" %in% learning_df$UttrCol, "Teebu", NA)
  LearnedVirdex <- ifelse("Virdex" %in% learning_df$UttrCol, "Virdex", NA)
  
  # sum up the "TRUE"s for each unique item to get uniqueLearnedN
  uniqueLearnedN <- "Virdex" %in% learning_df$UttrCol + "Teebu" %in% learning_df$UttrCol + "Pizer" %in% learning_df$UttrCol + "Fiffin" %in% learning_df$UttrCol
  
  LearnedLabels <- rbind(LearnedLabels, data.frame(subject = i, 
                                                   condition = unique(learning_df$condition),
                                                   LearningTrialsN = n_distinct(unique(learning_df$trialNum)),
                                                   uniqueLearnedN = uniqueLearnedN,
                                                   LearnedFiffin = LearnedFiffin, 
                                                   LearnedPizer = LearnedPizer, 
                                                   LearnedTeebu = LearnedTeebu, 
                                                   LearnedVirdex = LearnedVirdex,
                                                   MeanGazeValidity = MeanGazeValidity))
  
  
  # set up learning phase df for eyetrackingR  ############################################################################################################################################
  
  ## pull out test-phase AOI box bounds; 
  ## rect1, rect2, rect3, rect4 (i.e., the 4 novel learning items)
  ## eyetrackingR requires these in a separate dataframe
  
  learning_bounds <- unique(learning_df[, c(9:24)])
  
  ## subset columns of interest (e.g. we can lose the AOIs)
  
  learning_df_sel <- learning_df %>% select(c(1, 4, 33, 35, 41:45, 47:52, "leftGazeValidity_check", "rightGazeValidity_check", "cumulative_samples"))
  
  ## re-define column names to make them more intuitive
  
  colnames(learning_df_sel) <- c("subject", "condition", "timestamp",
                                 "trial", "topleft_obj", "topright_obj", "botleft_obj", "botright_obj",
                                 "label", "left_x", "left_y", "left_valid",
                                 "right_x", "right_y", "right_valid", 
                                 "leftValid_check", "rightValid_check", "gaze_sample_count")
  
  
  ## see 'Adding an Area-of-Interest', here: 
  ## http://www.eyetracking-r.com/vignettes/preparing_your_data
  
  ## configure topleft_obj aoi bounds to eyetrackingR standard
  
  topleft_aoi <- learning_bounds[1:4]
  colnames(topleft_aoi) <- c("left", "top", "right", "bottom")
  ## configure topright_obj aoi bounds to eyetrackingR standard
  
  topright_aoi <- learning_bounds[5:8]
  colnames(topright_aoi) <- c("left", "top", "right", "bottom")
  
  ## configure botleft_obj aoi bounds to eyetrackingR standard
  
  botleft_aoi <- learning_bounds[9:12]
  colnames(botleft_aoi) <- c("left", "top", "right", "bottom")
  
  ## configure botright_obj aoi bounds to eyetrackingR standard
  
  botright_aoi <- learning_bounds[13:16]
  colnames(botright_aoi) <- c("left", "top", "right", "bottom")
  
  
  ## add AOIs to main dataframe using eyetrackingR functionality
  ## note these are based on the RIGHT EYE ONLY
  
  ## 1 - topleft_aoi gaze (TRUE when the kid looks at topleft obj)
  
  learning_df_sel <- add_aoi(data = learning_df_sel, aoi_dataframe = topleft_aoi, 
                             x_col = "right_x", y_col = "right_y", # right eye
                             aoi_name = "topleft_gaze",
                             x_min_col = "left", x_max_col = "right", 
                             y_min_col = "top", y_max_col = "bottom")
  
  ## 2 - topright_aoi gaze (TRUE when kid looks to topright obj)
  
  learning_df_sel <- add_aoi(data = learning_df_sel, aoi_dataframe = topright_aoi, 
                             x_col = "right_x", y_col = "right_y", # right eye
                             aoi_name = "topright_gaze",
                             x_min_col = "left", x_max_col = "right", 
                             y_min_col = "top", y_max_col = "bottom")
  
  ## 3 - botleft_aoi gaze (TRUE when kid looks to botleft obj)
  
  learning_df_sel <- add_aoi(data = learning_df_sel, aoi_dataframe = botleft_aoi, 
                             x_col = "right_x", y_col = "right_y", # right eye
                             aoi_name = "botleft_gaze",
                             x_min_col = "left", x_max_col = "right", 
                             y_min_col = "top", y_max_col = "bottom")
  
  ## 3 - botright_aoi gaze (TRUE when kid looks to botright obj)
  
  learning_df_sel <- add_aoi(data = learning_df_sel, aoi_dataframe = botright_aoi, 
                             x_col = "right_x", y_col = "right_y", # right eye
                             aoi_name = "botright_gaze",
                             x_min_col = "left", x_max_col = "right", 
                             y_min_col = "top", y_max_col = "bottom")
  
  
  #MW: create new combined column for identifying each sample's gaze towards the 4 objects
  learning_df_sel <- learning_df_sel %>% mutate(fixation_obj = case_when(
    topleft_gaze == TRUE ~ "topleft",
    topright_gaze == TRUE ~ "topright",
    botleft_gaze == TRUE ~ "botleft",
    botright_gaze == TRUE ~ "botright",
    .default = "no_gaze"
  ))
  
  learning_df_filtered <- learning_df_sel %>% 
    filter(fixation_obj != "no_gaze")
  
  LearningBreadth <- learning_df_filtered %>% group_by(subject, condition, trial) %>% summarise(unique_gazes_per_trial = n_distinct(fixation_obj))
  
  combined_LearningBreadth <- bind_rows(combined_LearningBreadth, LearningBreadth)
  
  
  if (i == 59) {
    # Skip to the next iteration if participant ID is 59 (did not finish experiment; corrupt eye-tracking data that breaks the function)
    next
  }
  
  
  # TEST PHASE EXCLUSION & SUMMARIES  ############################################################################################################################################
  
  ## pull out test-phase AOI box bounds; 
  ## attention, left, right
  ## eyetrackingR requires these in a separate dataframe
  
  bounds <- unique(df[, c(5:8, 25:32)])
  
  ## subset test data for this pipeline
  
  df <- subset(df, is_test == 1) 
  
  ## subset columns of interest (e.g. we can lose the AOIs)
  
  df <- df %>% select(c(1, 4, 33, 35, 37, 39:40, 45, 47:52, "leftGazeValidity_check", "rightGazeValidity_check", "cumulative_samples"))
  
  ## re-define column names to make them more intuitive
  
  colnames(df) <- c("subject", "condition", "timestamp",
                    "trial", "target_location", "left_obj", "right_obj",
                    "label", "left_x", "left_y", "left_valid",
                    "right_x", "right_y", "right_valid", 
                    "leftValid_check", "rightValid_check", "gaze_sample_count")
  
  ## when there is no 'target_location', this means the attention-
  ## getter is up - let's make that clear
  
  df["target_location"][df["target_location"] == "NONE"] <- "ATTENTION"
  
  ## rename 'TestDuck' value 'Duck' (!)
  
  df["label"][df["label"] == "TestDuck"] <- "Duck"
  
  ## exclude the warm-up trial (i.e., the duck/teddy trial) in the Test-phase trial-level exclusion
  df <- subset(df, label != "Duck")
  
  ## make 'trackloss' column, based on left-eye/right-eye validity
  ## in this instance, if either falters we record trackloss
  ## but we can change this (e.g. just to right eye)
  
  df$trackloss <- ifelse(df$left_valid == 0 | df$right_valid == 0, 1, 0)
  
  ## configure attention AOI bounds to eyetrackingR standards
  ## see 'Adding an Area-of-Interest', here: 
  ## http://www.eyetracking-r.com/vignettes/preparing_your_data
  
  att_aoi <- bounds[1:4]
  colnames(att_aoi) <- c("left", "top", "right", "bottom")
  
  ## configure left aoi bounds to eyetrackingR standard
  
  left_aoi <- bounds[5:8]
  colnames(left_aoi) <- c("left", "top", "right", "bottom")
  
  ## configure right aoi bounds to eyetrackingR standard
  
  right_aoi <- bounds[9:12]
  colnames(right_aoi) <- c("left", "top", "right", "bottom")
  
  ## clear workspace
  
  rm(bounds)
  
  ## add AOIs to main dataframe using eyetrackingR functionality
  ## note these are based on the RIGHT EYE ONLY
  
  ## 1 - attention gaze (TRUE when the kid looks at attention-getter)
  
  df <- add_aoi(data = df, aoi_dataframe = att_aoi, 
                x_col = "right_x", y_col = "right_y", # right eye
                aoi_name = "attention_gaze",
                x_min_col = "left", x_max_col = "right", 
                y_min_col = "top", y_max_col = "bottom")
  
  ## 2 - left gaze (TRUE when kid looks to left test box)
  
  df <- add_aoi(data = df, aoi_dataframe = left_aoi, 
                x_col = "right_x", y_col = "right_y", # right eye
                aoi_name = "left_gaze",
                x_min_col = "left", x_max_col = "right", 
                y_min_col = "top", y_max_col = "bottom")
  
  ## 3 - right gaze (TRUE when kid looks to right test box)
  
  df <- add_aoi(data = df, aoi_dataframe = right_aoi, 
                x_col = "right_x", y_col = "right_y", # right eye
                aoi_name = "right_gaze",
                x_min_col = "left", x_max_col = "right", 
                y_min_col = "top", y_max_col = "bottom")
  
  ## remove attention samples from test phase data
  ## each test trial will then start when two objects 
  ## are on screen and the label is heard
  
  df = subset(df, target_location != 'ATTENTION')
  
  ## identify earliest timestamp within each trial
  ## and create 'START' trial message - this is
  ## necessary for zeroing our timestamp by trial
  ## see http://www.eyetracking-r.com/docs/subset_by_window
  
  df <- df %>% 
    group_by(subject, trial) %>%
    dplyr::mutate(
      trial_start = dplyr::first(timestamp), # get earliest timestamp in trial
    )
  
  df$message <- ifelse(df$timestamp == df$trial_start, "START", NA) # code trial start
  
  
  ##############
  
  # create new combined column for left/right fixation
  df <- df %>% mutate(lr_fixation = case_when(
    left_gaze == TRUE ~ "LEFT",
    right_gaze == TRUE ~ "RIGHT",
    left_gaze & right_gaze == FALSE ~ ""
  ))
  
  
  # Remove trials where they failed to fixate at both target & distractor
  df <- df %>%
    group_by(trial) %>%
    filter(all(c("LEFT", "RIGHT") %in% lr_fixation)) %>% ungroup()
  
  
  ################
  
  
  
  
  ## make 'eyetrackingr data', to enable other eyetrackingr functionality
  
  df <- make_eyetrackingr_data(df, 
                               participant_column = "subject",
                               trial_column = "trial",
                               time_column = "gaze_sample_count", 
                               trackloss_column = "trackloss",
                               aoi_columns = c('attention_gaze', 'left_gaze','right_gaze'),
                               treat_non_aoi_looks_as_missing = FALSE)
  
  ## subset windows, this will change the timestamp 
  ## with each trial, to start at zero
  
  df <- subset_by_window(df, 
                         window_start_msg = "START", 
                         msg_col = "message", 
                         rezero = TRUE)
  
  ## again, remove unwanted columns 
  
  df <- select(df, -c(trial_start, message))
  
  
  
  
  ## clean by trackloss, and assess trackloss rates
  ## see http://www.eyetracking-r.com/vignettes/window_analysis
  
  df <- clean_by_trackloss(data = df) # removed "trial_prop_thresh = .3" to manually calculate number of participants who need to be excluded due to <70% gaze validity
  
  trackloss_analysis(data = df) # by trial
  
  current_trackloss <- trackloss_analysis(data = df) # by trial; MW temporary code for outputting table to word
  # write.table(table_trackloss, file = "table_trackloss.csv", sep = ",", quote = FALSE, row.names = F)
  combined_trackloss <- rbind(combined_trackloss, current_trackloss)
  
  ## add hit column
  ## this will tell you if the kid is looking
  ## where they should be looking [left/right]
  ## given the item locations and label they are hearing
  
  df$hit <-ifelse(df$target_location == 'LEFT' & df$left_gaze == TRUE |
                    df$target_location == 'RIGHT' & df$right_gaze == TRUE,
                  1, 0)
  
  combined_testdf <- bind_rows(combined_testdf, df) # append current trial test-phase df to a master df
}


# Remove unncessary dataframes --------------------------------------------
rm(att_aoi, df_complete, df_filled, df_interpolated, interp_summary_merged, left_aoi, left_interp_summary, right_aoi, right_interp_summary)

# check how many pts had overall MeanGazeValidity of <70%, then exclude them
LearnedLabels <- LearnedLabels %>% mutate(Excl.MeanGazeValidity = MeanGazeValidity < 0.7)
table(LearnedLabels$Excl.MeanGazeValidity, LearnedLabels$condition) # "TRUE" = number of participants with overall mean gaze validity of <70%
LearnedLabels <- LearnedLabels %>% filter(Excl.MeanGazeValidity == FALSE)
LearnedLabels$Excl.MeanGazeValidity <- NULL # delete unused column

# check how many pts learned less than 3 items in the Learning Phase, then exclude them
LearnedLabels <- LearnedLabels %>% mutate(Excl.SufficientLearning = uniqueLearnedN < 3)
table(LearnedLabels$Excl.SufficientLearning) # "TRUE" = number of participants who learned less than 3 items

table(LearnedLabels$Excl.SufficientLearning, LearnedLabels$condition) # "TRUE" = number of participants who learned less than 3 items by condition

LearnedLabels <- LearnedLabels %>% filter(Excl.SufficientLearning == FALSE)
LearnedLabels$Excl.SufficientLearning <- NULL # delete unused column

n_per_cond <- LearnedLabels %>% group_by(condition, subject) %>% summarise(n = n()) %>% group_by(condition) %>% summarise(n_mean = mean(n()))
n_per_cond <- first(n_per_cond$n_mean)
# output csv of df grouped by participant
write.table(LearnedLabels, file = paste("LearnedLabels", n_per_cond, start_file, end_file, ".csv", sep = "_"), sep = ",", quote = FALSE, row.names = F)

trials_per_pt <- combined_trackloss %>% group_by(subject) %>% summarise(num_trials = n())


# check how many pts had trials of >30% trackloss, then exclude -----------
excl_combined_trackloss <- merge(LearnedLabels, combined_trackloss)
n_distinct(excl_combined_trackloss$subject)
excl_combined_trackloss %>%
  group_by(condition) %>%
  summarise(n_distinct_participants = n_distinct(subject))

pre_trial_trackloss_excl <- excl_combined_trackloss %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup()

excl_combined_trackloss <- excl_combined_trackloss %>% mutate(Excl.TrialCheckloss = TracklossForTrial > .7)
table(excl_combined_trackloss$Excl.TrialCheckloss, excl_combined_trackloss$condition) # "TRUE" = number of trials w/ <30% of usable looking samples

excl_combined_trackloss <- excl_combined_trackloss %>%  filter(Excl.TrialCheckloss == FALSE)

excl_combined_trackloss %>%
  group_by(condition) %>%
  summarise(n_distinct_participants = n_distinct(subject))


post_trial_trackloss_excl <- excl_combined_trackloss %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup()
  


pre_trial_trackloss_excl <- excl_combined_trackloss %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup()

# combine excl_combine_trackloss with combined_testdf (to remove excluded trials from combined_testdf) -----------------------
remaining_trials <- excl_combined_trackloss %>% select(subject, condition, trial)

# no. of unique trials in each condition
combined_testdf %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup() %>% 
  group_by(condition) %>% 
  summarise(n_sum_trials = sum(n_trials))
# no. of unique trials for each participant
combined_testdf %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup()
# no. of participants in each condition
combined_testdf %>%
  group_by(condition) %>%
  summarise(n_distinct_participants = n_distinct(subject))

# merge remaining trials & combined_testdf to select only the trials that remained after initial exclusions
excl_combined_testdf <- merge(remaining_trials, combined_testdf)
# no. of unique trials in each condition
excl_combined_testdf %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup() %>% 
  group_by(condition) %>% 
  summarise(n_sum_trials = sum(n_trials))
# no. of unique trials for each participant
excl_combined_testdf %>%
  group_by(condition, subject) %>%
  summarise(n_trials = n_distinct(trial)) %>% ungroup()
# no. of participants in each condition
excl_combined_testdf %>%
  group_by(condition) %>%
  summarise(n_distinct_participants = n_distinct(subject))


# combine Test df with Learned Labels
onlyLearned_df <- merge(excl_combined_testdf, LearnedLabels)



# check number of pts in each condition -----------------------------------
onlyLearned_df %>% group_by(subject, condition, trial) %>% summarise(n=n()) %>%
  group_by(subject, condition) %>% summarise(n=n()) %>% group_by(condition) %>% summarise(n=n())


# create new column which marks Test-phase trials where the pt had selected the novel label in the Learning phase at least once
onlyLearned_df <- onlyLearned_df %>% mutate(LearnedLabel = if_else(label == LearnedFiffin | 
                                                                   label == LearnedPizer |
                                                                   label == LearnedTeebu |
                                                                   label == LearnedVirdex, T, F))
table(onlyLearned_df$LearnedLabel)


# only keep trials containing learned labels
onlyLearned_df <- subset(onlyLearned_df,
                          label == LearnedFiffin | 
                          label == LearnedPizer |
                          label == LearnedTeebu |
                          label == LearnedVirdex)

length(unique(onlyLearned_df$subject))
onlyLearned_df %>% group_by(subject, condition, trial) %>% summarise(n=n()) %>%
  group_by(subject, condition) %>% summarise(n=n()) %>% group_by(condition) %>% summarise(n=n())

# output csv of learned 
write.table(onlyLearned_df, file = paste0("onlyLearned_df", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)

# summary of hits in only trials with learned labels 
LearnedHits_Pt <- onlyLearned_df %>% group_by(condition, subject, hit) %>% summarise(num_trials = n()) %>% pivot_wider(names_from = hit, values_from = num_trials, names_prefix = "hit_")
LearnedHits_Pt.Trial <- onlyLearned_df %>% group_by(condition, subject, trial, hit) %>% summarise(num_trials = n()) %>% pivot_wider(names_from = hit, values_from = num_trials, names_prefix = "hit_")
write.table(LearnedHits_Pt, file = paste0("LearnedHits_Pt", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)
write.table(LearnedHits_Pt.Trial, file = paste0("LearnedHits_Pt.Trial", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)

















# CALCULATE PROPRTION LOOKING---------------------------------------------------
onlyLearned_df <- onlyLearned_df %>% relocate(gaze_sample_count, .after = condition) # move gaze_sample_count to an earlier column

sum(is.na(onlyLearned_df$timestamp))

onlyLearned_df_arranged <- onlyLearned_df %>% group_by(subject, trial) %>% arrange(gaze_sample_count, .by_group = T) %>% ungroup()

onlyLearned_df_arranged <- onlyLearned_df_arranged %>% 
  mutate(ms_timestamp = gaze_sample_count * 10/12, .after = gaze_sample_count) # generate ms_timestamps

# add column: trial+pre-/post-label
onlyLearned_df <- onlyLearned_df_arranged %>% mutate(PrePostLabel =
                      case_when(
                        ms_timestamp <=2500 ~ "PreLabel",
                        ms_timestamp >=2740 & ms_timestamp <= 5000 ~ "PostLabel"
                      ), .after = trial)
# output csv of learned df with pre/post labels
write.table(onlyLearned_df, file = paste0("onlyLearned_w.prepost_df", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)


str(onlyLearned_df)
table(onlyLearned_df$PrePostLabel)
sum(is.na(onlyLearned_df$PrePostLabel))

# rename "trial" to "testTrial" to distinguish from LearningTrialsN (the number of total trials in the Learning Phase)
onlyLearned_df <- onlyLearned_df %>% rename(testTrial = trial)

# remove rows not in pre- or post-label windows
onlyLearned_df <- onlyLearned_df %>% filter(!is.na(PrePostLabel))

onlyLearned_df %>% group_by(testTrial) %>% summarise(n = n())
onlyLearned_df %>% group_by(testTrial, PrePostLabel, hit) %>% summarise(n = n())


# CALCULATE PROPORTION LOOKING TIME DATA -----------------------
hit_summary <- onlyLearned_df %>% filter(!is.na(hit)) %>% 
  group_by(condition, subject, LearningTrialsN, testTrial, label, PrePostLabel, hit) %>% 
  summarise(count = n()) %>% ungroup()

hit_summary_wide <- hit_summary %>% pivot_wider(names_from = hit, values_from = count, names_prefix = "hit_")
hit_summary_wide <- hit_summary_wide %>% mutate(across(
  c(hit_1, hit_0), ~ ifelse(is.na(.), 0, .))
)# replace NA with 0 (might not be the correct thing to do tho)
hit_summary_wide <- hit_summary_wide %>% mutate(propLooking = hit_1 / (hit_1 + hit_0))


# Identify pre/post sections of trials where pt didn't look at both the target and distraction --------
# create new column summing up propLooking accross each trial's pre/post stages
hit_summary_wide <- hit_summary_wide %>% group_by(subject, testTrial) %>% 
  mutate(PrePostCombinedLookingProp = sum(propLooking)) %>% ungroup()
# create new column to identify trials that were either all "hit_0" or "hit_1"; i.e., sum prop of "0" or "2" respectively.
hit_summary_wide <- hit_summary_wide %>% group_by(subject, testTrial) %>% 
  mutate(Excl.PrePostCombinedLookingProp = 
           case_when(
             PrePostCombinedLookingProp == 2 | PrePostCombinedLookingProp == 0 ~ "Exclude",
             .default = ""
           )) %>% ungroup()

table(hit_summary_wide$Excl.PrePostCombinedLookingProp, hit_summary_wide$condition)

hit_summary_wide <- hit_summary_wide %>%  filter(Excl.PrePostCombinedLookingProp != "Exclude")

hit_summary_wide %>% group_by(subject, condition, testTrial) %>% summarise(n=n()) %>%
  group_by(subject, condition) %>% summarise(n=n()) %>% group_by(condition) %>% summarise(n=n())



hit_summary_wide2 <- hit_summary_wide %>% select(-c(hit_1, hit_0, PrePostCombinedLookingProp, Excl.PrePostCombinedLookingProp)) %>% 
  pivot_wider(names_from = PrePostLabel, values_from = propLooking)
# Identify trials that don't have both pre- and post-label sections -------
# anything that didn't have either section turns up as NA for BaselineCorrProp
hit_baselineCorr <- hit_summary_wide2 %>% mutate(BaselineCorrProp = PostLabel - PreLabel)

# create new column to identify trials in which the pt didn't look at both, and there's only one of either pre- or post-label sections.
hit_baselineCorr <- hit_baselineCorr %>% ungroup() %>% 
  mutate(Excl.NotBothPrePostOnlyTargetOrDistractor = 
           case_when(
             (PreLabel == 0 & is.na(BaselineCorrProp)) ~ "Exclude",
             (PreLabel == 1 & is.na(BaselineCorrProp)) ~ "Exclude",
             (PostLabel == 0 & is.na(BaselineCorrProp)) ~ "Exclude",
             (PostLabel == 1 & is.na(BaselineCorrProp)) ~ "Exclude",
             .default = ""
           ))
table(hit_baselineCorr$Excl.NotBothPrePostOnlyTargetOrDistractor, hit_baselineCorr$condition)

hit_baselineCorr <- hit_baselineCorr %>%  filter(Excl.NotBothPrePostOnlyTargetOrDistractor != "Exclude") %>% select(-Excl.NotBothPrePostOnlyTargetOrDistractor)


# create new column to identify trials in which there's only one of either pre- or post-label sections.
hit_baselineCorr <- hit_baselineCorr %>% ungroup() %>% 
  mutate(Excl.NotBothPrePost = 
           case_when(
             (is.na(BaselineCorrProp)) ~ "Exclude",
             .default = ""
           ))
table(hit_baselineCorr$Excl.NotBothPrePost, hit_baselineCorr$condition)

hit_baselineCorr <- hit_baselineCorr %>%  filter(Excl.NotBothPrePost != "Exclude") %>% select(-Excl.NotBothPrePost)




# group by participant to get avg prop. looking
hit_baselineCorr_byPt <- hit_baselineCorr %>% group_by(condition, subject) %>% 
    summarise(mean_BaselineCorr_Prop = mean(BaselineCorrProp), trialsN = n())


# CALCULATE PROPORTION LOOKING TIME DATA, GROUPED BY CONDITION -----------------------
hit_byCond_summary <- onlyLearned_df %>% filter(!is.na(hit)) %>% 
  group_by(subject, condition, testTrial, PrePostLabel, hit) %>% 
  summarise(count = n()) %>% ungroup()
hit_byCond_summary
# hit_summary %>% group_by(testTrial, PrePostLabel) %>% summarise(countagain = n())

hit_byCond_summary_wide <- hit_byCond_summary %>% pivot_wider(names_from = hit, values_from = count, names_prefix = "hit_")
hit_byCond_summary_wide <- hit_byCond_summary_wide %>% mutate(across(
  c(hit_1, hit_0), ~ ifelse(is.na(.), 0, .))
)# replace NA with 0 (might not be the correct thing to do tho)
hit_byCond_summary_wide <- hit_byCond_summary_wide %>% mutate(propLooking = hit_1 / (hit_1 + hit_0))
hit_byCond_summary_wide2 <- hit_byCond_summary_wide %>% select(-c(hit_1, hit_0)) %>% 
  pivot_wider(names_from = PrePostLabel, values_from = propLooking)

hit_byCond_baselineCorr <- hit_byCond_summary_wide2 %>% mutate(BaselineCorrProp = PostLabel - PreLabel)

hit_byCond_baselineCorr <- hit_byCond_baselineCorr %>% filter(!is.na(BaselineCorrProp))


# group by participant to get avg prop. looking
hit_byCondt_baselineCorr_byPt <- hit_byCond_baselineCorr %>% group_by(subject, condition) %>% 
  summarise(mean_BaselineCorr_Prop = mean(BaselineCorrProp), trialsN = n()) %>% ungroup()

hit_byCondt_baselineCorr_byPt$condition <- as.factor(hit_byCondt_baselineCorr_byPt$condition)
hit_byCondt_baselineCorr_byPt$subject <- as.factor(hit_byCondt_baselineCorr_byPt$subject)



# output csv of pre-/post-label sample summary
write.table(hit_summary_wide, file = paste0("hit_summary_wide", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)

# output csv of baseline-corrected looking prop. 
write.table(hit_baselineCorr, file = paste0("hit_baselineCorr", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)

# output csv of baseline-corrected looking prop., grouped by participant
write.table(hit_baselineCorr_byPt, file = paste0("hit_baselineCorr_byPt", start_file, "-", end_file, ".csv"), sep = ",", quote = FALSE, row.names = F)




# # ANALYSIS ----------------------------------------------------------------
# load libraries ---------------------------------------------------------------
install.packages("devtools")
devtools::install_github("ndphillips/yarrr", 
                         build_vignettes = TRUE)

library(tidyverse)
library(purrr)
library(lme4)
library(lmerTest)
library(ggpubr)
library(ggeffects)
library(car)
library(BayesFactor)
library(papaja)
library(jtools)
library(MuMIn)
library(yarrr)
library(sjPlot)

# set working directory --------------------------------------------------------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
# import csv  ----------------------------------------
df <- read.csv("./hit_baselineCorr1-96.csv", fileEncoding = "UTF-8")
df_log <- read.csv("./Data/CuriGaze_log_Cleaned.csv", fileEncoding = "UTF-8")

# rename columns
df <- df %>% rename(participant = subject, 
                    item = label)

# specify data structure
df <- df %>% mutate(across(c(condition, participant, testTrial, item), as.factor))

table(df$condition)
table(df$condition, df$testTrial)


# merge main df & log -----------------------------------------------------
df <- merge(df, df_log)


# descriptives ------------------------------------------------------------
df_pt_demographics <- df %>% select(participant, condition, age, gender) %>% distinct()
## age --------------------------------------------------------------------
df_pt_demographics %>% summarise(Mean = mean(age), SD = sd(age), n())
df_pt_demographics %>% group_by(condition) %>% summarise(Mean = mean(age), SD = sd(age), n()) %>% as.data.frame()

# gender ------------------------------------------------------------------
table(df_pt_demographics$gender)
# f  m 
# 30 45 
table(df_pt_demographics$condition, df_pt_demographics$gender)
#           f  m
# curiosity  9 16
# random    11 14
# yoked     10 15

# condition means
df %>% group_by(condition) %>% summarise(Mean = mean(BaselineCorrProp), SD = sd(BaselineCorrProp), n())


# Calculate SD's of >3 in the data ----------------------------------------

df <- df %>%
  group_by(participant) %>% # when avg'd by participant
  mutate(OUTLIER = case_when(BaselineCorrProp >= mean(BaselineCorrProp, na.rm = TRUE) + (3 * sd(BaselineCorrProp, na.rm = TRUE)) ~ "OUTLIER",
                             BaselineCorrProp <= mean(BaselineCorrProp, na.rm = TRUE) - (3 * sd(BaselineCorrProp, na.rm = TRUE)) ~ "OUTLIER",
                             TRUE ~ ""
  )) %>% ungroup() # no outliers

df <- df %>% # across the whole sample
  mutate(OUTLIER = case_when(BaselineCorrProp >= mean(BaselineCorrProp, na.rm = TRUE) + (3 * sd(BaselineCorrProp, na.rm = TRUE)) ~ "OUTLIER",
                             BaselineCorrProp <= mean(BaselineCorrProp, na.rm = TRUE) - (3 * sd(BaselineCorrProp, na.rm = TRUE)) ~ "OUTLIER",
                             TRUE ~ ""
  )) %>% ungroup() # no outliers


# Average number of triggered events at learning & testing by Condition -------------
df_grp_pt <- df %>% group_by(condition, participant, LearningTrialsN) %>% summarise(MeanProp = mean(BaselineCorrProp), TestTrialsN = n()) %>% ungroup()

df_grp_pt %>% group_by(condition) %>% summarise(AvgNTriggered_Learning = mean(LearningTrialsN),AvgNTriggered_Learning_SD = sd(LearningTrialsN), AvgNTriggered_Test = mean(TestTrialsN), n())
df_grp_pt %>% summarise(AvgNTriggered_Learning = mean(LearningTrialsN), AvgNTriggered_Learning_SD = sd(LearningTrialsN), AvgNTriggered_Test = mean(TestTrialsN), n())
table(df_grp_pt$condition, df_grp_pt$LearningTrialsN)
table(df_grp_pt$condition, df_grp_pt$TestTrialsN)

# one-sample t-test to check whether sample is significantly different from 0 ************************************************
df_grp_pt %>% group_by(condition) %>% summarise(Mean = mean(MeanProp), SD = sd(MeanProp), n())
#   condition   Mean    SD `n()`
# 1 curiosity 0.0849 0.175    25
# 2 random    0.0799 0.121    25
# 3 yoked     0.0984 0.140    25



ggdensity(df_grp_pt$MeanProp, 
          main = "Density plot of Participant-level Looking Prop",
          xlab = "Looking Prop")


ggqqplot(df_grp_pt$MeanProp, 
         main = "Q-Q plot of Participant-level Looking Prop")

# Shapiro-Wilk’s Normality test
shapiro.test(df_grp_pt$MeanProp)
# W = 0.97895, p-value = 0.24575 - not significant - data is normal

# one-sample t-test, participant-level across all conditions
t.test(df_grp_pt$MeanProp, mu = 0, alternative = "two.sided")
df_grp_pt %>% summarise(M = mean(MeanProp), SD = sd(MeanProp))
# t = 5.2275, df = 74, p-value = 1.534e-06


# one-sample t-test, participant-level ONLY CURIOSITY 
hit_Curiosity_ONLY <- df_grp_pt %>% filter(condition == "curiosity")
ttest_Curi_result <- t.test(hit_Curiosity_ONLY$MeanProp, mu = 0, alternative = "two.sided")
ttest_Curi_result
hit_Curiosity_ONLY %>% summarise(M = mean(MeanProp), SD = sd(MeanProp))
# t = 2.423, df = 24, p-value = 0.0233
## bonferroni correction (ONLY CURIOSITY)
p.adjust(ttest_Curi_result$p.value, method = "bonferroni")
## bonferroni adjusted p-value = .02330216
# Bayes Factor (ONLY CURIOSITY)
ttestBF(x = hit_Curiosity_ONLY$MeanProp, mu = 0)
## Alt., r=0.707 : 2.368083 ±0%

# one-sample t-test, participant-level ONLY YOKED 
hit_Yoked_ONLY <- df_grp_pt %>% filter(condition == "yoked")
ttest_Yoked_result <- t.test(hit_Yoked_ONLY$MeanProp, mu = 0, alternative = "two.sided")
hit_Yoked_ONLY %>% summarise(M = mean(MeanProp), SD = sd(MeanProp))
# t = 3.5065, df = 24, p-value = 0.001813
## bonferroni correction (ONLY Yoked)
p.adjust(ttest_Yoked_result$p.value, method = "bonferroni")
## bonferroni adjusted p-value = .001813153
# Bayes Factor (ONLY Yoked)
ttestBF(x = hit_Yoked_ONLY$MeanProp, mu = 0)
## Alt., r=0.707 : 20.64214 ±0%

# one-sample t-test, participant-level ONLY RANDOM 
hit_Random_ONLY <- df_grp_pt %>% filter(condition == "random")
ttest_Random_result <- t.test(hit_Random_ONLY$MeanProp, mu = 0, alternative = "two.sided")
hit_Random_ONLY %>% summarise(M = mean(MeanProp), SD = sd(MeanProp))
# t = 3.3111, df = 24, p-value = 0.002932
## bonferroni correction (ONLY Random)
p.adjust(ttest_Random_result$p.value, method = "bonferroni")
## bonferroni adjusted p-value = .00293167
# Bayes Factor (ONLY Random)
ttestBF(x = hit_Random_ONLY$MeanProp, mu = 0)
## Alt., r=0.707 : 13.61001 ±0%

# one-sample three-factor ANOVA ************************************************
# Examine mean & SDs by conditon (note that this is AFTER grouping by participant, NOT by trial)
df_grp_pt %>% group_by(condition) %>%
  summarise(
    count = n(),
    mean = mean(MeanProp, na.rm = TRUE),
    sd = sd(MeanProp, na.rm = TRUE)
  )

leveneTest(MeanProp ~ condition, data = df_grp_pt)
#       Df F value  Pr(>F)  
# group  2  1.6772 0.1941; no sig. diff. variance across groups
#       72 

# compute ANOVA
anova.cond <- aov(MeanProp ~ condition, data = df_grp_pt)
# Summary of the analysis
summary(anova.cond)
summary(anova.cond)[[1]][["Pr(>F)"]][1] # confirm p-value: 0.9000946
plot(anova.cond, 1)


# Normality (assessed with Shapiro-Wilk test) 
# Extract the residuals
anova.cond_residuals <- residuals(object = anova.cond)
# Run Shapiro-Wilk test
shapiro.test(x = anova.cond_residuals)
# W = 0.98101, p-value = 0.3216 ### >.05; normality not violated

# compute BF10 for ANOVA
anova.cond_BF <- anovaBF(MeanProp ~ condition, data = df_grp_pt, whichRandom = "participant")
anova.cond_BF[1] # BF10: 0.1239862 
1/anova.cond_BF[1] #BF01: 8.065411 



# Plot of BF across different number of participants in analysis
## Generate sequental number counter for each participant (distinct for each of the 3 groups)
df_grp_pt <- df_grp_pt %>% group_by(condition) %>% 
  mutate(grp_ID = row_number()) %>% 
  mutate(grp_ID = 1:n()) %>% 
  mutate(grp_ID = seq_len(n())) %>% 
  mutate(grp_ID = seq_along(condition))

BF_combined <- data.frame()

for (i in 1:25) {
  print(i)
  # subset dataset to desired n
  df_grp_pt_BF <- subset(df_grp_pt, grp_ID <= i)
  # calculate BF10
  BF_current <- as.data.frame(
    extractBF(
      anovaBF(MeanProp ~ condition, data = df_grp_pt_BF, whichRandom = "participant")))
  # add n counter
  BF_current <- BF_current %>% mutate(seq_n = nrow(df_grp_pt_BF))
  BF_combined <- rbind(BF_combined, BF_current)
}
BF_combined

# tidy combined BF df
BF_tidy <- BF_combined %>% select(seq_n, bf)
# add BF01
BF_tidy <- BF_tidy %>% mutate(bf01 = 1/bf)

# plot BF01 against sequential analysis at different n
ggplot(BF_tidy, aes(x = seq_n, y = bf01)) +
  geom_line(size = 1.5, colour = "#217bb3") +
  geom_point(size = 3.5, fill = "white", colour = "#217bb3", stroke = 1) +
  labs(x = "Data Collection Sequence (N)", 
       y = "Bayes Factor (BF01)") + 
 scale_x_continuous(breaks = seq(min(BF_tidy$seq_n), max(BF_tidy$seq_n), by = 3),
                     minor_breaks = NULL) +
  geom_hline(aes(yintercept = 0.3, color = "BF = 0.3"), size = 1.5) +
  geom_hline(aes(yintercept = 3, color = "BF = 3"), size = 1.5) +
  geom_hline(aes(yintercept = 10, color = "BF = 10"), size = 1.5) +
  scale_color_manual(name = "Bayes Factor Thresholds",
                     values = c("BF = 0.3" = "#a52528", 
                                "BF = 3" = "#137116",
                                "BF = 10" = "#dba653"),
                     breaks = c("BF = 0.3", "BF = 3", "BF = 10")) +   
  theme_minimal(base_size = 20) +
  theme(panel.grid.major.x = element_blank(),
        legend.position = c(0.05, 0.9),
        legend.justification = c(0, 1),
        legend.title = element_text(size = 17),
        axis.text.y = element_text(size = 15),
        axis.text.x = element_text(size = 13))

  
# Violin pirate plot of looking prop by condition (Figure 2) -------------------------

# par(mar = c(5.1, 5.5, 4.1, 2.1))
pirateplot(formula = MeanProp ~ condition,
           data = df_grp_pt,
           xlab = "Condition",
           ylab = "Baseline-Corrected Looking Proportion",
           pal="xmen",
           theme=3,
           point.cex = 1.5,
           point.pch = 21,
           point.o = .15,
           jitter.val = .07,
           inf.method = "ci", #changed from the default Bayesian high density interval to confidence interval
           inf.f.o = .5,
           inf.disp = "bean",
           cex.axis = 1,
           cex.lab = 1.2,
           cex.names = 1.1,
           width.max = 0.25
)
abline(h = 0, col = "red", lwd = 2, lty = 2) # add horizontal line at 0

# generate normally distributed random numbers to look for issues in DV distribution
df$rnorm <- rnorm(nrow(df), mean = 0, sd = 1)

# dot plot ()
ggplot(df, aes(x = rnorm, y = BaselineCorrProp, color = condition)) +
  geom_point(size = 3) +
  labs(title = "Look for issues with clustering/distribution",
       x = "rnorm",
       y = "BaselineCorrProp",
       color = "Condition") +
  theme_minimal()





################################################################################
# mutate new col with binary specification (negative=0, positive=1)
df <- df %>% mutate(BaselineCorrProp.Binary = case_when(
  BaselineCorrProp < 0 ~ 0,
  BaselineCorrProp >= 0 ~ 1
))

# Raw/% of correct test-phase trials by condition -------------------------

df.binary <- df %>% select(condition, participant, testTrial, item, BaselineCorrProp.Binary, BaselineCorrProp)

# count number of test trials of each item that a participant completed

df.binary <- df.binary %>% group_by(participant, item) %>% 
  mutate(item_trials_seen = n()) %>% 
  ungroup()


# Stats for TABLE 2
# prop. learned items by condition - 
#Learned = infant had positive (>0) baseline-corrected looking prop. towards target for both test trials OR, 
#if they only saw 1 test trial and looked positively towards target, it still counts as learned
prop_learned_summary <- df.binary %>% 
  group_by(condition, participant, item, item_trials_seen) %>% 
  summarise(test_item_learned = prod(BaselineCorrProp.Binary)) %>% 
  ungroup()
prop_learned_summary

prop_learned_by_participant <- prop_learned_summary %>%
  group_by(condition, participant) %>%
  summarize(
    prop_correct = mean(test_item_learned, na.rm = TRUE),
    items_learned = sum(test_item_learned),
    n = n()
  ) %>% ungroup()
prop_learned_by_participant

avg_items <- prop_learned_by_participant %>% 
  group_by(condition) %>% 
  summarize(
    avg_items_per_Cond = mean(n),
    avg_items_per_Cond_SD = sd(n),
    avg_labs_ret = mean(items_learned),
    avg_labs_ret_SD = sd(items_learned),
  )
avg_items

prop_learned_by_condition <- prop_learned_summary %>%
  group_by(condition) %>%
  summarize(
    prop_correct = mean(test_item_learned, na.rm = TRUE),
    prop_corr_SD = sd(test_item_learned, na.rm = TRUE),
    n = n(),
    avg_items = n/25, # divide by number of pts in each condition (i.e., n=25)
    avg_items_learned = sum(test_item_learned)/25, # divide by number of pts in each condition (i.e., n=25)
  ) %>% ungroup()
prop_learned_by_condition



# Reviewer 2 - plots for proportion of labels retained
pirateplot(formula = MeanProp ~ condition,
           data = pirateplot(formula = prop_correct ~ condition,
           data = prop_learned_by_participant,
           xlab = "Condition",
           ylab = "Proportion of Labels Retained",
           pal="xmen",
           theme=3,
           point.cex = 1.5,
           point.pch = 21,
           point.o = .15,
           jitter.val = .07,
           inf.method = "ci", #changed from the default Bayesian high density interval to confidence interval
           inf.f.o = .5,
           inf.disp = "bean",
           cex.axis = 1,
           cex.lab = 1.2,
           cex.names = 1.1,
           width.max = 0.25
))
abline(h = 0, col = "red", lwd = 2, lty = 2) # add horizontal line at 0


# Simple logistic regression (for supplementary materials)
glm.bi <-  
  glm(prop_correct ~ condition, 
      family = binomial(link = "logit"),
      data = prop_learned_by_participant)

summary(glm.bi)

glm.null <-  
  glm(prop_correct ~ 1, 
      family = binomial(link = "logit"),
      data = prop_learned_by_participant)
## Test Random Effects via Likelihood Ratio Tests (LRT) -------------------------
### Test effect of adding Condition to null model ----------------------------------------------
anova(glm.null, glm.bi, test="LRT") # p=.8903 - No Sig. improvement
exp((BIC(glm.null) - BIC(glm.bi))/2) # BF10 = 0.01454606

#### Print model table ---------------------------------------------------------
apa_print(glm.bi)
#### get SE using summ from jtools ---------------------------------------------
summ(glm.bi)
r.squaredGLMM(glm.bi)

################################################################################

# plot binomial data
cdplot(condition ~ BaselineCorrProp.Binary, data=df)


# Trial-level baseline-corrected looking proportion at target by participant (Figure 3) --------
ggplot(df, aes(x = participant, y = BaselineCorrProp, fill = condition)) +
  scale_fill_manual(values = c("curiosity" = "#81b6e5", "random" = "#fa8f81", "yoked" = "#87dd86")) +
  geom_boxplot(show.legend = F, coef = 1) + # coef = 0 shows all datapoints instead of whiskers +
  facet_grid(. ~ condition, scales = "free_x") +
  labs(x = "Participant", y = "Looking Proportion") +
  geom_hline(yintercept = 0, linetype = "dashed", color = "red") +
  theme_minimal() +
  theme(strip.text = element_text(size = 18), # increase condition label font size
        axis.title.y = element_text(size = 18), # increase looking prop label font size
        axis.title.x = element_text(size = 18), # increase participant label font size
        axis.text.x = element_text(size = 12, angle = 45, hjust = 1), # rotate x-axis labels
        axis.text.y = element_text(size = 16), # y-axis label font size
        panel.grid.major.x = element_blank(), # remove vertical grid lines
        panel.grid.minor.x = element_blank())

# Trial-level baseline-corrected looking proportion at target by participant with individual datapoints (Figure 3 - FOR REVIEWER 1) --------
ggplot(df, aes(x = participant, y = BaselineCorrProp, fill = condition)) +
  scale_fill_manual(values = c("curiosity" = "#81b6e5", "random" = "#fa8f81", "yoked" = "#87dd86")) +
  geom_boxplot(show.legend = F, coef = 0) + # coef = 0 shows all datapoints instead of whiskers
  geom_point(show.legend = F, color = "black", alpha = 0.6) +
  facet_grid(. ~ condition, scales = "free_x") +
  labs(x = "Participant", y = "Looking Proportion") +
  geom_hline(yintercept = 0, linetype = "dashed", color = "red") +
  theme_minimal() +
  theme(strip.text = element_text(size = 18), # increase condition label font size
        axis.title.y = element_text(size = 18), # increase looking prop label font size
        axis.title.x = element_text(size = 18), # increase participant label font size
        axis.text.x = element_text(size = 12, angle = 45, hjust = 1), # rotate x-axis labels
        axis.text.y = element_text(size = 16), # y-axis label font size
        panel.grid.major.x = element_blank(), # remove vertical grid lines
        panel.grid.minor.x = element_blank())


## GLMER Binary Base Model with Random Effects only (no main effects): --------
## Binary Base Model with Random intercept for Participant: -------------------
gm.RE.Participant <- glmer(
  BaselineCorrProp.Binary ~ (1|participant), # Random intercept for Participant
  family = binomial(link="logit"),
  glmerControl(optimizer="bobyqa"),
  data = df)
summary(gm.RE.Participant) # singular fit

allFit(gm.RE.Participant)
## Binary Base Model with Random intercept for Item: -------------------
gm.RE.Item <- glmer(
  BaselineCorrProp.Binary ~ (1|item), # Random intercept for item 
  family = binomial(link="logit"),
  glmerControl(optimizer="bobyqa"),
  data = df)
summary(gm.RE.Item) # singular fit

allFit(gm.RE.Item)


## Binary Min Theoretical/ a priori Model: -------------------
gm.min <- glmer(
  BaselineCorrProp.Binary ~ condition +
    (1 + condition|item), # Random intercept for Item + random slope for Condition by Item
  family = binomial(link="logit"),
  glmerControl(optimizer="bobyqa"),
  data = df)
summary(gm.min) # singular fit

allFit(gm.min)

# Exploratory Growth Curve Analysis -----------------------------------------
# load libraries ---------------------------------------------------------------
library(tidyverse)
library(eyetrackingR)
library(lme4)

# set working directory --------------------------------------------------------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# import csv  ----------------------------------------
df_ori <- read.csv("./onlyLearned_w.prepost_df1-96.csv", fileEncoding = "UTF-8")
df_log <- read.csv("./Data/CuriGaze_log_Cleaned.csv", fileEncoding = "UTF-8")
df_log <- df_log %>% select(participant)

# rename columns
df_ori <- df_ori %>% rename(participant = subject, 
                    item = label)
df <- inner_join(df_ori, df_log, by = "participant")

# Check data structure ----------------------------------------------------
colnames(df)

# remove unnecessary columns
df <- df %>% select(-c(LearnedFiffin, LearnedPizer, LearnedTeebu, LearnedVirdex, LearnedLabel))
df %>% group_by(condition) %>%
  summarise(n_distinct_participants = n_distinct(participant))

# create categorical column for hit (i.e., sample looking at target vs. distractor) --------
df <- df %>% mutate(TargetDistractor = case_when(
  hit == 0 ~ "Distractor",
  hit == 1 ~ "Target"
), .after = hit)

# create individual AOI columns for target & distractor hits (necessary for eyetrackingR function)
df <- df %>% mutate(AOI_Target = case_when(
  TargetDistractor == "Target" ~ TRUE,
  TargetDistractor == "Distractor" ~ FALSE
), .after = TargetDistractor)

df <- df %>% mutate(AOI_Distractor = case_when(
  TargetDistractor == "Target" ~ FALSE,
  TargetDistractor == "Distractor" ~ TRUE
), .after = TargetDistractor)
str(df)

# specify data structure
df <- df %>% mutate(across(c(condition, participant, trial, PrePostLabel, target_location, left_obj, right_obj,
                             item, TargetDistractor), as.factor))
str(df)


# re-run make_eyetrackingr_data to conform to GCA function requirements -------------------------------------------

ET_data <- make_eyetrackingr_data(df, 
                       participant_column = "participant",
                       trial_column = "trial",
                       time_column = "ms_timestamp",
                       trackloss_column = "trackloss",
                       aoi_columns = c('AOI_Target','AOI_Distractor'),
                       treat_non_aoi_looks_as_missing = TRUE
)
str(ET_data)


# Select only Post-label-onset (2740-5000ms) using the eyetrackingR subset_by_window() function ------------------------------
ET_data_PostLabel <- subset_by_window(ET_data,
                                      window_start_time = 2740,
                                      window_end_time = 5000,
                                      rezero = FALSE)

# following eyetrackingR documentation for GCA "visualize the timecourse" ------------

# Only post-label ---------------------------------------------------------
# aggregate across trials within subjects in time analysis
response_time_PostLabel <- make_time_sequence_data(ET_data_PostLabel, time_bin_size = 40, 
                                 predictor_columns = c("condition", "item")
                                 , aois = "AOI_Target"
                                 # , other_dv_columns = "item"
                            )
# visualize time results
plot(response_time_PostLabel, predictor_column = "condition")

plot(response_time_PostLabel, predictor_column = "condition") +
  theme_light() +
  coord_cartesian(ylim = c(0.3,0.7))


# TEST baseline correction for timecourse visualization -------------------
df_PreLabel_baselineCorr <- read.csv("./hit_baselineCorr1-96.csv", fileEncoding = "UTF-8")
df_PreLabel_baselineCorr <- df_PreLabel_baselineCorr %>% select(condition, subject, testTrial, PreLabel)
df_PreLabel_baselineCorr <- df_PreLabel_baselineCorr %>% rename(participant = subject, 
                                            trial = testTrial)
df_PreLabel_baselineCorr <- df_PreLabel_baselineCorr %>% mutate(across(c(condition, participant, trial), as.factor)) # instead factorised them here, so that structure correctly only included 75 participants levels


response_time_PostLabel_corr <- inner_join(response_time_PostLabel, df_PreLabel_baselineCorr)


response_time_PostLabel_corr <- response_time_PostLabel_corr %>% 
  mutate(BaselineCorrProp = Prop - PreLabel)


response_time_PostLabel_corr_avg_prop_by_trial <- response_time_PostLabel_corr %>%
  group_by(participant, condition, Time) %>%
  summarise(avg_prop = mean(BaselineCorrProp, na.rm = TRUE),
            sd_prop = sd(BaselineCorrProp, na.rm = TRUE)) %>% 
  ungroup() %>% 
  drop_na()

# Post-label-onset Time Course of Baseline-corrected Proportional Target Looking by Condition (Figure 4)
ggplot(response_time_PostLabel_corr_avg_prop_by_trial, aes(x = Time, y = avg_prop, color = condition)) +
  scale_fill_manual(values = c("curiosity" = "#81b6e5", "random" = "#fa8f81", "yoked" = "#87dd86")) +
  scale_color_manual(values = c("curiosity" = "#619cff", "random" = "#fa8f81", "yoked" = "#87dd86")) +
  geom_smooth(method = "loess", se = TRUE, span = 0.2, aes(fill = condition), alpha = 0.15, size = 1.2) +
  geom_hline(yintercept = 0, colour = "red", linetype = "dotted", size = 1) +
  labs(
       x = "Time (ms)",
       y = "Baseline-corrected Proportion of Looking Towards Target") +
  theme_minimal() +
  theme(
    axis.text = element_text(size = 12),
    axis.title.x = element_text(size = 14),
    axis.title.y = element_text(size = 14),
    panel.grid.major.x = element_blank(),
    panel.grid.minor.x = element_blank(),
    legend.text = element_text(size = 14),
    legend.title = element_blank()
  ) 

# GCA model
# Optimizer improves convergence of the model
contr=lmerControl(optimizer="bobyqa",
                  optCtrl=list(maxfun=1000000))
# modelling using the eyetracking_R syntax
gca.m1 <- lmer(Elog ~ condition * (ot1 + ot2 + ot3) + # with condition as fixed effect
                              (ot1 + ot2 | participant) +
                              (ot1 + ot2 | item),
                            data = response_time_PostLabel, REML = FALSE,
                            control = contr)
summary(gca.m1) # singular fit
