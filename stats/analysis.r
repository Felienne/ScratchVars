library(nparcomp)

root <- "/Users/aserebrenik/Desktop/Onderzoek/ScratchVars/"
setwd(paste(root,"stats/",sep=""))

#comparing distribution of the variable names' length
icpc2017varlens <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/var-len.dat",sep=""),header=TRUE,sep="\t")
scratchvarlens <- read.csv(paste(root,"data_plus_pandas_files/output/distributions\ of\ lengths.csv",sep=""),header=TRUE)

#lbl <- c(rep("PHP",1557390),rep("Java",196545), rep("perl",88754))
#v <- c(rep(5,1305365),rep(6,252025),rep(5,100572),rep(6,95973),rep(5,55774),rep(6,32980))

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
#Java - C           0.190  0.189  0.191   581.035       0
#JS - C            -0.077 -0.077 -0.076  -278.928       0
#perl - C          -0.088 -0.089 -0.087  -226.516       0
#PHP - C            0.122  0.122  0.123   567.042       0
#scratch - C        0.234  0.232  0.235   394.418       0
#JS - Java         -0.267 -0.268 -0.266  -759.737       0
#perl - Java       -0.278 -0.280 -0.277  -618.628       0
#PHP - Java        -0.068 -0.069 -0.067  -224.780       0
#scratch - Java     0.044  0.042  0.045    70.802       0
#perl - JS         -0.012 -0.013 -0.011   -29.672       0
#PHP - JS           0.199  0.198  0.200   769.479       0
#scratch - JS       0.310  0.309  0.312   516.336       0
#PHP - perl         0.211  0.210  0.212   551.758       0
#scratch - perl     0.322  0.320  0.324   476.859       0
#scratch - PHP      0.111  0.110  0.113   192.089       0

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

icpc2017characters <- read.csv(paste(root,"sophiko-icpc-2017/extract_variables/result-files/char-use.dat",sep=""),header=TRUE)

library(rapport)
lambda.test(icpc2017characters,1)

forLambdaLower <- t(subset(icpc2017characters, select=c(Clower,JSlower,Javalower,PHPlower,perllower)))
colnames(forLambdaLower) <- icpc2017characters$ch
