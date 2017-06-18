library(nparcomp)

root <- "/Users/aserebrenik/Desktop/Onderzoek/ScratchVars/"
setwd(paste(root,"stats/",sep=""))

#comparing distribution of the variable names' length
icpc2017varlens <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/var-len.dat",sep=""),header=TRUE,sep="\t")
scratchvarlens <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ lengths_percentage.csv",sep=""),header=TRUE)
scratchproclens <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ lengths\ of\ functions_percentage.csv",sep=""),header=TRUE)

lbl <- c()
v <- c()
#for (i in c(2:ncol(icpc2017varlens))) { lbl <- c(rep(names(icpc2017varlens)[[i]], sum(icpc2017varlens[[i]])), lbl) }

r <- nrow(icpc2017varlens)
c <- ncol(icpc2017varlens)
for (i in c(1:r)) {
	for (j in c(2:c)) { 
		lbl <- c(rep(names(icpc2017varlens)[[j]], icpc2017varlens[i,j]), lbl)
		v <- c(rep(icpc2017varlens[i,1], icpc2017varlens[i,j]), v)
	}
	cat(".")
}

cat("^")
r <- nrow(scratchvarlens)
for (i in c(1:r)) {
	lbl <- c(rep("scratch", scratchvarlens[i,2]), lbl)
	v <- c(rep(scratchvarlens[i,1], scratchvarlens[i,2]), v)
	cat(".")
}

d <- data.frame(v, lbl)

res <- mctp(d$v~d$lbl, data=d, type="Tukey", asy.method="fisher")

res$Analysis

#               Estimator  Lower  Upper Statistic p.Value
#Java - C           0.191  0.190  0.192   585.138       0
#JS - C            -0.077 -0.078 -0.076  -280.612       0
#perl - C          -0.089 -0.090 -0.088  -227.084       0
#PHP - C            0.123  0.123  0.124   571.295       0
#scratch - C        0.212  0.211  0.213   842.946       0
#JS - Java         -0.268 -0.269 -0.267  -766.611       0
#perl - Java       -0.280 -0.281 -0.279  -623.981       0
#PHP - Java        -0.068 -0.069 -0.067  -225.660       0
#scratch - Java     0.021  0.020  0.022    65.337       0
#perl - JS         -0.012 -0.013 -0.011   -29.535       0
#PHP - JS           0.200  0.200  0.201   783.570       0
#scratch - JS       0.289  0.288  0.290  1011.954       0
#PHP - perl         0.212  0.211  0.213   556.088       0
#scratch - perl     0.301  0.300  0.302   753.143       0
#scratch - PHP      0.089  0.088  0.089   412.693       0


# X < Y if Upper < 0 and X > Y if Lower > 0
# The loops below produce two sets of edges for the T-graph
# Copy paste them into digraph.py and generete the T-graph from Python

s_xy <- subset(res$Analysis, Upper < 0)
names <- strsplit(rownames(s_xy), " - ")
for (i in 1:length(names)){
  cat(paste("\"",names[[i]][2],"\" -> ",sep=""), paste("\"",names[[i]][1],"\"",sep=""), "\n")
}

s_yx <- subset(res$Analysis, Lower > 0)
names <- strsplit(rownames(s_yx), " - ")
for (i in 1:length(names)){
  cat(paste("\"",names[[i]][1],"\" -> ",sep=""), paste("\"",names[[i]][2],"\"",sep=""), "\n")
}

#digraph G {
#"C" ->  "JS" 
#"C" ->  "perl" 
#"Java" ->  "JS" 
#"Java" ->  "perl" 
#"Java" ->  "PHP" 
#"JS" ->  "perl" 
#"Java" ->  "C" 
#"PHP" ->  "C" 
#"scratch" ->  "C" 
#"scratch" ->  "Java" 
#"PHP" ->  "JS" 
#"scratch" ->  "JS" 
#"PHP" ->  "perl" 
#"scratch" ->  "perl" 
#"scratch" ->  "PHP" 
#}

#dropping transitive dependencies
#digraph G {
#"C" ->  "JS" 
#"Java" ->  "PHP" 
#"JS" ->  "perl" 
#"PHP" ->  "C" 
#"scratch" ->  "Java" 
#}

######################

lbl <- c()
v1 <- c()
v2 <- c()


r <- nrow(scratchvarlens)
for (i in c(1:r)) {
	lbl <- c(rep("var", scratchvarlens[i,2]), lbl)
	v1 <- c(rep(scratchvarlens[i,1], scratchvarlens[i,2]), v1)
	cat(".")
}
cat("^")
r <- nrow(scratchproclens)
for (i in c(1:r)) {
	lbl <- c(rep("proc", scratchproclens[i,2]), lbl)
	v2 <- c(rep(scratchproclens[i,1], scratchproclens[i,2]), v2)
	cat(".")
}

wilcox.test(v1,v2,alternative="l")
v<- c(v1,v2)
d <- data.frame(v, lbl)
res <- npar.t.test(d$v~d$lbl, data=d, alternative="l")
res$Analysis


#	Wilcoxon rank sum test with continuity correction
#
#data:  v1 and v2
#W = 306063624946, p-value < 2.2e-16
#alternative hypothesis: true location shift is less than 0

# res$Analysis
#       Effect Estimator Lower Upper        T p.Value
#1 p(proc,var)     0.109     0 0.109 -1039.98       0
######################
icpc2017characters <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/char-use.dat",sep=""),header=TRUE)
scratchcharacters <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ one\ letter\ chars_upper\ and\ lower.csv",sep=""),header=TRUE)
#scratchaz <- subset(scratchcharacters, grepl("[a-z]",ch))
icpc2017characters$Scratchupper <- scratchcharacters$uppercase
icpc2017characters$Scratchlower <- scratchcharacters$lowercase 
nameless <- subset(icpc2017characters, select=-c(ch)) 
row.names(nameless) <- icpc2017characters$ch

chisq.test(t(nameless))

#	Pearson's Chi-squared test
#
#data:  t(nameless)
#X-squared = 749847.8, df = 275, p-value < 2.2e-16


forLambdaLower <- t(subset(icpc2017characters, select=c(Clower,JSlower,Javalower,PHPlower,perllower,Scratchlower)))
colnames(forLambdaLower) <- icpc2017characters$ch

library(rapport)
lambda.test(icpc2017characters,1)

library(lsa)
cosine(as.matrix(nameless))
#                Cupper    Clower   JSupper   JSlower Javaupper Javalower  PHPupper  PHPlower perlupper  perllower Scratchupper Scratchlower
#Cupper       1.0000000 0.3611283 0.8412634 0.7173503 0.6803331 0.3109723 0.2205311 0.5245342 0.6528813 0.17944583   0.54529066    0.3956803
#Clower       0.3611283 1.0000000 0.4464655 0.7136214 0.2934833 0.9804554 0.9498817 0.9012264 0.1643316 0.54133089   0.15098804    0.8121212
#JSupper      0.8412634 0.4464655 1.0000000 0.9125161 0.5582298 0.4534770 0.3424506 0.6697455 0.7221644 0.30745926   0.43835905    0.4290080
#JSlower      0.7173503 0.7136214 0.9125161 1.0000000 0.5307265 0.7319082 0.6413899 0.8691923 0.6185908 0.40601382   0.32851288    0.6159914
#Javaupper    0.6803331 0.2934833 0.5582298 0.5307265 1.0000000 0.2605340 0.1741584 0.3622637 0.4050535 0.18065945   0.32026099    0.2806996
#Javalower    0.3109723 0.9804554 0.4534770 0.7319082 0.2605340 1.0000000 0.9761646 0.9206813 0.2097267 0.56162536   0.16932736    0.8421509
#PHPupper     0.2205311 0.9498817 0.3424506 0.6413899 0.1741584 0.9761646 1.0000000 0.8569645 0.1249727 0.55025114   0.13367539    0.8302615
#PHPlower     0.5245342 0.9012264 0.6697455 0.8691923 0.3622637 0.9206813 0.8569645 1.0000000 0.4505609 0.52431810   0.29721860    0.8017757
#perlupper    0.6528813 0.1643316 0.7221644 0.6185908 0.4050535 0.2097267 0.1249727 0.4505609 1.0000000 0.32989451   0.63747997    0.4211002
#perllower    0.1794458 0.5413309 0.3074593 0.4060138 0.1806594 0.5616254 0.5502511 0.5243181 0.3298945 1.00000000   0.07275307    0.4479274
#Scratchupper 0.5452907 0.1509880 0.4383591 0.3285129 0.3202610 0.1693274 0.1336754 0.2972186 0.6374800 0.07275307   1.00000000    0.6199330
#Scratchlower 0.3956803 0.8121212 0.4290080 0.6159914 0.2806996 0.8421509 0.8302615 0.8017757 0.4211002 0.44792740   0.61993302    1.0000000
#ScratchUpper is closest to PerlUpper, ScratchLower and Cupper
#ScratchLower is closest to Javalower, Clower, PHPUpper, PHPlower
 
nameless_dist <- dist(t(nameless)) #default uses the Euclidean distance
plot(hclust(nameless_dist)) #default complete linkage
# suggests that scratch upper case is similar to other upper cases and lower case to Java lower case
 
plot(hclust(dist(t(nameless), method="euc"), method="ward"))

rowMeans(cosine(as.matrix(nameless)))
#      Cupper       Clower      JSupper      JSlower    Javaupper    Javalower     PHPupper     PHPlower    perlupper    perllower Scratchupper Scratchlower 
#   0.5357842    0.6095861    0.5934282    0.6738178    0.4205335    0.6180853    0.5667251    0.6815401    0.4780630    0.4251399    0.3928166    0.6247208 
sort(rowMeans(cosine(as.matrix(nameless))))
#Scratchupper    Javaupper    perllower    perlupper       Cupper     PHPupper      JSupper       Clower    Javalower Scratchlower      JSlower     PHPlower 
#   0.3928166    0.4205335    0.4251399    0.4780630    0.5357842    0.5667251    0.5934282    0.6095861    0.6180853    0.6247208    0.6738178    0.6815401 
