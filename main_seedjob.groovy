pipelineJob ('dsl_job_a')
{
    scm { 
        git 
          {    
             remote
              {    
                 url("https://github.com/shahirahmed/testrepo.git")
                 credentials("ec46fa17-e17a-4a26-89ef-1c8226c6bc3b") 
              }
          }
      }

}