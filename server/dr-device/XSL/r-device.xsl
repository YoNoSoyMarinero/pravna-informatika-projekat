<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="text"/>
	<xsl:template match="/">
		<xsl:apply-templates select="rulebase"/>
	</xsl:template>
	<xsl:template match="rulebase">
		<xsl:if test="@rdf_import">(import-rdf <xsl:value-of select="@rdf_import"/>)</xsl:if>
		<xsl:text>
		</xsl:text>
		<xsl:if test="@rdf_export">(export-rdf <xsl:value-of select="@rdf_export"/>
			<xsl:text>  </xsl:text>
			<xsl:value-of select="@rdf_export_classes"/>)</xsl:if>
		<xsl:text>
		</xsl:text>
		<xsl:apply-templates select="imp"/>
	</xsl:template>
	<xsl:template match="imp">
(<xsl:apply-templates select="_rlab"/>
		<xsl:apply-templates select="_body"/>
  => 
	<xsl:apply-templates select="_head"/>
) 
	</xsl:template>
	<xsl:template match="_rlab">
		<xsl:if test="@maintainable='no'">ntm-</xsl:if>
		<xsl:value-of select="@ruletype"/>
		<xsl:text> </xsl:text>
		<xsl:value-of select="ind"/>
		<xsl:text>
		</xsl:text>
		<!--
		<xsl:if test="@superior">
			<xsl:text>(declare (superior </xsl:text>
			<xsl:value-of select="@superior"/>
			<xsl:text>)) 
			</xsl:text>
		</xsl:if>-->
	</xsl:template>
	<xsl:template match="_body">
		<xsl:apply-templates select="atom|naf|and"/>
	</xsl:template>
	<xsl:template match="and">
		<xsl:apply-templates select="atom|naf"/>
	</xsl:template>
	<xsl:template match="_head">
		<xsl:if test="calc">(calc <xsl:apply-templates select="calc"/>)</xsl:if>
		<xsl:apply-templates select="atom"/>
	</xsl:template>
	<xsl:template match="calc">
		<xsl:apply-templates select="function_call"/>
	</xsl:template>
	<xsl:template match="naf">
		(not
		<xsl:apply-templates select="atom"/>
		)
	</xsl:template>
	<xsl:template match="atom"> 
	<xsl:if test="_id">
	 <xsl:apply-templates select="_id/var|_id/ind"/> 
	 <xsl:text> "&lt;-" </xsl:text>
	</xsl:if>
	(<!--<xsl:if test="string-length(normalize-space(_opr/rel))=0">
			<xsl:value-of select="_opr/rel/@href"/>
		</xsl:if>-->
		<!--<xsl:if test="string-length(normalize-space(_opr/rel))>0">-->
		<xsl:apply-templates select="_opr/rel"/>
		<!--</xsl:if>-->
		<!--<xsl:if test="string-length(normalize-space(_opr/rel))=0">?</xsl:if>-->
		<xsl:text> </xsl:text>
		<xsl:apply-templates select="_path|_slot|_varslot"/>
	)
 </xsl:template>
	<xsl:template match="_slot">
		(<xsl:value-of select="@name"/>
		<xsl:apply-templates select="var|ind|_not|_and|or|aggregate_function_call"/>
		)
	</xsl:template>
	<xsl:template match="_path">
	((<xsl:apply-templates select="slotname|genpath|recpath"/>)
		<xsl:apply-templates select="var|ind|_not|_and|or|aggregate_function_call"/>
	)
	</xsl:template>
	<xsl:template match="_varslot">
		(?<xsl:value-of select="@name"/>
		<xsl:apply-templates select="var|ind|_not|_and|or|aggregate_function_call"/>
		)
	</xsl:template>
	<xsl:template match="slotname">
		<xsl:apply-templates select="var|ind"/>
	</xsl:template>
	<xsl:template match="genpath">
		<xsl:if test="var/@type=multi">
			<xsl:apply-templates select="var"/>
		</xsl:if>
		<xsl:if test="var/@type=single">
			$<xsl:apply-templates select="var"/>
		</xsl:if>
	</xsl:template>
	<xsl:template match="recpath">
	(<xsl:apply-templates select="slotname"/>)
	</xsl:template>
	<xsl:template match="var">
		<xsl:if test="@type='single'">
		<xsl:text> ?</xsl:text>
		</xsl:if>
		<xsl:if test="@type='multi'">
		<xsl:text> $?</xsl:text>
		</xsl:if>
		<xsl:if test="@type='single-multi'">
		<xsl:text> ??</xsl:text>
		</xsl:if>
		<xsl:value-of select="."/>
	</xsl:template>
	<xsl:template match="ind">
		<xsl:text> </xsl:text>
		<xsl:value-of select="."/>
	</xsl:template>
	<xsl:template match="function_call">
		(<xsl:value-of select="@name"/>
		<xsl:text> </xsl:text>
		<xsl:apply-templates select="ind|var|function_call"/>
		)
	</xsl:template>
	<xsl:template match="aggregate_function_call">
		(<xsl:value-of select="@name"/>
		<xsl:text> </xsl:text>
		<xsl:apply-templates select="var"/>
		)
	</xsl:template>
	<xsl:template match="_not">
		<xsl:text> ~</xsl:text>
		<xsl:apply-templates select="var|ind"/>
	</xsl:template>
	<xsl:template match="_and">
		<xsl:text> </xsl:text>
		<xsl:for-each select="var|ind|_not|function_call">
			<xsl:choose>
				<xsl:when test="name(.)=&quot;var&quot;">
					<xsl:text> ?</xsl:text>
					<xsl:value-of select="."/>
				</xsl:when>
				<xsl:when test="name(.)=&quot;ind&quot;">
					<xsl:text> </xsl:text>
					<xsl:value-of select="."/>
				</xsl:when>
				<xsl:when test="name(.)=&quot;function_call&quot;">
					<xsl:text> :</xsl:text>
					<xsl:variable name="func_pos" select="position()"/>
					<xsl:apply-templates select="../*[position()=$func_pos]"/>
				</xsl:when>
				<xsl:when test="name(.)=&quot;_not&quot;">
					<xsl:text> ~</xsl:text>
					<xsl:apply-templates select="var|ind"/>
				</xsl:when>
			</xsl:choose>
			<xsl:if test="not (position()=last())">
				<xsl:text> &amp; </xsl:text>
			</xsl:if>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
