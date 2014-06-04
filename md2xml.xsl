<?xml version="1.0" encoding="utf-8"?>
<!--
Stylesheet to transform an XHTML document to XML one.
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">

  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
  <xsl:param name="id">ID</xsl:param>
  <xsl:param name="date">DATE</xsl:param>
  <xsl:param name="title">TITLE</xsl:param>

  <!-- catch the root element -->
  <xsl:template match="/xhtml">
    <xsl:text disable-output-escaping="yes">
    &lt;!DOCTYPE weblog PUBLIC "-//CAFEBABE//DTD weblog 1.0//EN"
                               "../dtd/weblog.dtd">
    </xsl:text>
    <weblog>
      <xsl:attribute name="id"><xsl:value-of select="$id"/></xsl:attribute>
      <xsl:attribute name="date"><xsl:value-of select="$date"/></xsl:attribute>
      <title><xsl:value-of select="$title"/></title>
      <xsl:apply-templates/>
    </weblog>
  </xsl:template>

  <xsl:template match="h1">
    <p><imp><xsl:apply-templates/></imp></p>
  </xsl:template>

  <xsl:template match="h2">
    <p><imp><xsl:apply-templates/></imp></p>
  </xsl:template>

  <xsl:template match="h3">
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

