<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">

 <xsl:import href="theme.xsl"/>
 <xsl:import href="text.xsl"/>
 <xsl:output method="xml" encoding="UTF-8"/>

 <!-- catch the root element -->
 <xsl:template match="/xhtml">
  <!--
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE weblog PUBLIC "-//CAFEBABE//DTD weblog 1.0//EN"
                          "../dtd/weblog.dtd">
  -->
  <weblog id=""
          date="">
   <title></title>
   <xsl:apply-templates/>
  </weblog>
 </xsl:template>

 <xsl:template match="h1">
  <p><imp><xsl:apply-templates/></imp></p>
 </xsl:template>

 <xsl:template match="p">
  <p><xsl:apply-templates/></p>
 </xsl:template>

 <xsl:template match="em">
  <term><xsl:apply-templates/></term>
 </xsl:template>

 <xsl:template match="strong">
  <imp><xsl:apply-templates/></imp>
 </xsl:template>

</xsl:stylesheet>

