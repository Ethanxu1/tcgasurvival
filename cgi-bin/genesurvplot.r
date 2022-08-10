args <-commandArgs(trailingOnly = TRUE)
cohort=toupper(args[1])
gene=toupper(args[2])
fn=args[3]

load(paste0("./exprData/",cohort,".RData"))
expdat=mrna_n

if(!grepl("\\D",gene)){
geneid=as.numeric(gene)
gene=as.vector(expdat$gene[expdat$geneid==geneid])}

pp=data.frame(clinicData[,c("vital_status","days_to_death","days_to_last_followup")])
for(i in 1:ncol(pp)){pp[,i]=as.numeric(as.vector(pp[,i]))}
pp$days_to_last_followup[is.na(pp$days_to_last_followup)]=pp$days_to_death[is.na(pp$days_to_last_followup)]
x=as.numeric(as.vector(expdat[expdat$gene==gene,][3:ncol(expdat)]))
x=log2(x)
cutoff=median(x)
x[x<cutoff]=0;x[x>=cutoff]=1

library(survival)
ev=1*(pp$vital_status==1)
fut=pp$days_to_last_followup
su=Surv(fut,ev)
jpeg(paste0("./tmp/",fn,".jpg"),width=700,height=500,quality=100)
plot(survfit(su~x),lwd=2,lty=1:2,cex.lab=1.5,cex.main=1.5,cex.axis=1.3,main=paste(gene,"Median expression cutoff:",round(cutoff,digits=4)),
  xlab="Time (Days to last followup)",ylab="Survival probability")
ntab=table(x);ns=paste("[n=",ntab,"]",sep="")
legend("bottomleft",lty=1:2,lwd=2,legend=paste(c("Low expression","High expression"),ns))
graphics.off()

#optimal cutoff
library(cutpointr)
x=as.numeric(as.vector(expdat[expdat$gene==gene,][3:ncol(expdat)]))
x=log2(x)
cutoff=cutpointr(data.frame(x=x,g=pp$vital_status),x,g)$optimal_cutpoint
x[x<cutoff]=0;x[x>=cutoff]=1
jpeg(paste0("./tmp/",fn,"_n.jpg"),width=700,height=500,quality=100)
plot(survfit(su~x),lwd=2,lty=1:2,cex.lab=1.5,cex.main=1.5,cex.axis=1.3,main=paste(gene,"Optimal expression cutoff:",round(cutoff,digits=4)),
  xlab="Time (Days to last followup)",ylab="Survival probability")
ntab=table(x);ns=paste("[n=",ntab,"]",sep="")
legend("bottomleft",lty=1:2,lwd=2,legend=paste(c("Low expression","High expression"),ns))
graphics.off()


