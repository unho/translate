<?php
// Arquivo de idioma de Nucleus en galego
//
// Autor: Contidos Dixitais
// Versión de Nucleus: v1.0-v3.2
//
// NOTA: se desexas traducir este arquivo ao teu idioma, ten en conta que
// nas próximas versións de Nucleus, algunhas variables poden ser engadidas, mentres que outras
// poden ser eliminadas. En consecuencia, é importante que indiques no documento para que versión 
// de Nucleus foi feita a tradución.
//
// Os arquivos que estén completamente traducidos pódense enviar a Nucleus e eles ocuparanse de
// facelos accesibles para descargar (poñendo nos créditos ao autor, por suposto)

// START changed/added after 3.15 START

define('_LIST_PLUG_SUBS_NEEDUPDATE','Por favor, usa o botón\'Actualizar a lista de subscrición\'- para actualizar a lista de extensións.');
define('_LIST_PLUGS_DEP',			'A extensión(s) require(n):');

// END changed/added after 3.15

// START changed/added after 3.1 START

// comments list per weblog
define('_COMMENTS_BLOG',			'Todos os comentarios da bitácora');
define('_NOCOMMENTS_BLOG',			'Non se fixeron comentarios nesta bitácora');
define('_BLOGLIST_COMMENTS',		'Comentarios');
define('_BLOGLIST_TT_COMMENTS',		'Lista de todos os comentarios feitos nesta bitácora');


// for use in archivetype-skinvar
define('_ARCHIVETYPE_DAY',			'día');
define('_ARCHIVETYPE_MONTH',		'mes');

// tickets (prevents malicious users to trick an admin to perform actions he doesn't want)
define('_ERROR_BADTICKET',			'Tícket non válido.');

// plugin dependency
define('_ERROR_INSREQPLUGIN',		'Fallou a instalación da extensión, requírese ');
define('_ERROR_DELREQPLUGIN',		'Fallou a detección da extensión, requerido por ');

// cookie prefix
define('_SETTINGS_COOKIEPREFIX',	'Prefixo da "cookie"');

// account activation
define('_ERROR_NOLOGON_NOACTIVATE',	'Imposible enviar a ligazón de activación. Non é posible iniciar a sesión.');
define('_ERROR_ACTIVATE',			'A clave de activación non existe, non é válida, ou está caducada.');
define('_ACTIONLOG_ACTIVATIONLINK', 'Enviouse a ligazón de activación');
define('_MSG_ACTIVATION_SENT',		'Enviouse por correo-e unha ligazón de activación.');

// activation link emails
define('_ACTIVATE_REGISTER_MAIL',	"Ola <%memberName%>,\n\nNecesitas activar a túa conta en <%siteName%> (<%siteUrl%>).\nPodes facelo premendo na ligazón que aparece máis abaixo: \n\n\t<%activationUrl%>\n\nTes 2 días para facelo. Despois, a ligazón de activación quedará invalidada.");
define('_ACTIVATE_REGISTER_MAILTITLE',	"Activa a túa '<%memberName%>' conta");
define('_ACTIVATE_REGISTER_TITLE',	'Benvido/a <%memberName%>');
define('_ACTIVATE_REGISTER_TEXT',	'Xa case está. Por favor, escolle un contrasinal para a túa conta.');
define('_ACTIVATE_FORGOT_MAIL',		"Ola <%memberName%>,\n\n Podes escoller un novo contrasinal para a túa conta <%siteName%> (<%siteUrl%>) premendo na ligazón que aparece máis abaixo.\n\n\t<%activationUrl%>\n\nTes 2 días para facelo. Despois, a ligazón de activación quedará invalidada.");
define('_ACTIVATE_FORGOT_MAILTITLE',"Reactiva a túa conta '<%memberName%>'");
define('_ACTIVATE_FORGOT_TITLE',	'Benvido/a <%memberName%>');
define('_ACTIVATE_FORGOT_TEXT',		'Podes escoller un novo contrasinal para a túa conta máis abaixo:');
define('_ACTIVATE_CHANGE_MAIL',		"Ola <%memberName%>,\n\nO teu correo-e foi modificado, así que terás que reactivar a túa conta en <%siteName%> (<%siteUrl%>).\nPodes facelo premendo na seguinte ligazón: \n\n\t<%activationUrl%>\n\nTes 2 días para facelo. Despois, a ligazón de activación quedará invalidada.");
define('_ACTIVATE_CHANGE_MAILTITLE',"Reactiva a túa conta '<%memberName%>'");
define('_ACTIVATE_CHANGE_TITLE',	'Benvido/a <%memberName%>');
define('_ACTIVATE_CHANGE_TEXT',		'Verificouse o teu cambio de correo-e. Grazas!');
define('_ACTIVATE_SUCCESS_TITLE',	'Activación realizada');
define('_ACTIVATE_SUCCESS_TEXT',	'A túa conta foi activada satisfactoriamente.');
define('_MEMBERS_SETPWD',			'Contrasinal');
define('_MEMBERS_SETPWD_BTN',		'Contrasinal');
define('_QMENU_ACTIVATE',			'Activación de conta');
define('_QMENU_ACTIVATE_TEXT',		'<p>Logo de activar a túa conta, podes comezar a usala <a href="index.php?action=showlogin">iniciando a sesión</a>.</p>');

define('_PLUGS_BTN_UPDATE',			'Actualizar lista de subscrición');

// global settings
define('_SETTINGS_JSTOOLBAR',		'Estilo de barra de ferramentas Javascript');
define('_SETTINGS_JSTOOLBAR_FULL',	'Barra de ferramentas completa (IE)');
define('_SETTINGS_JSTOOLBAR_SIMPLE','Barra de ferramentas simple (Non-IE)');
define('_SETTINGS_JSTOOLBAR_NONE',	'Deshabilitar barra de ferramentas');
define('_SETTINGS_URLMODE_HELP',	'(Info: <a href="documentation/tips.html#searchengines-fancyurls">Como activar URLs atractivas</a>)');

// extra plugin settings part when editing categories/members/blogs/...
define('_PLUGINS_EXTRA',			'Preferencias para os plugins extra');

// itemlist info column keys
define('_LIST_ITEM_BLOG',			'bitácora:');
define('_LIST_ITEM_CAT',			'cat:');
define('_LIST_ITEM_AUTHOR',			'autor:');
define('_LIST_ITEM_DATE',			'data:');
define('_LIST_ITEM_TIME',			'hora:');

// indication of registered members in comments list
define('_LIST_COMMENTS_MEMBER', 	'(membro)');

// batch operations
define('_BATCH_WITH_SEL',			'Coa selección:');
define('_BATCH_EXEC',				'Executar');

// quickmenu
define('_QMENU_HOME',				'Inicio');
define('_QMENU_ADD',				'Engadir elemento');
define('_QMENU_ADD_SELECT',			'-- seleccionar --');
define('_QMENU_USER_SETTINGS',		'Configuración');
define('_QMENU_USER_ITEMS',			'Elementos');
define('_QMENU_USER_COMMENTS',		'Comentarios');
define('_QMENU_MANAGE',				'Xestión');
define('_QMENU_MANAGE_LOG',			'Inicio de sesión');
define('_QMENU_MANAGE_SETTINGS',	'Configuración global');
define('_QMENU_MANAGE_MEMBERS',		'Membros');
define('_QMENU_MANAGE_NEWBLOG',		'Nova bitácora');
define('_QMENU_MANAGE_BACKUPS',		'Copias de seguridade');
define('_QMENU_MANAGE_PLUGINS',		'Extensións');
define('_QMENU_LAYOUT',				'Aparencia');
define('_QMENU_LAYOUT_SKINS',		'Peles');
define('_QMENU_LAYOUT_TEMPL',		'Patróns');
define('_QMENU_LAYOUT_IEXPORT',		'Importar/Exportar');
define('_QMENU_PLUGINS',			'Extensións');

// quickmenu on logon screen
define('_QMENU_INTRO',				'Introdución');
define('_QMENU_INTRO_TEXT',			'<p>Esta é a pantalla de inicio de Nucleus CMS, o sistema de xestión de contidos que está a ser empregado para manter este sitio web.</p><p>Se posúes unha conta, podes comezar a sesión e publicar novos elementos.</p>');

// helppages for plugins
define('_ERROR_PLUGNOHELPFILE',		'Imposible atopar axuda para esta extensión');
define('_PLUGS_HELP_TITLE',			'Páxina de axuda para extensións');
define('_LIST_PLUGS_HELP', 			'axuda');


// END changed/started after 3.1

// START changed/added after v2.5beta START

// general settings (security)
define('_SETTINGS_EXTAUTH',			'Habilitar a autenticación externa');
define('_WARNING_EXTAUTH',			'Advertencia: habilitar só se é necesario.');

// member profile
define('_MEMBERS_BYPASS',			'Usar autenticación externa');

// 'always include in search' blog setting (yes/no) [in v2.5beta, the 'always' part wasn't clear]
define('_EBLOG_SEARCH',				'Incluír <em>sempre</em> na procura');

// END changed/added after v2.5beta

// START introduced after v2.0 START

// media library
define('_MEDIA_VIEW',				'ver');
define('_MEDIA_VIEW_TT',			'Ver o arquivo (abriráse noutra ventá)');
define('_MEDIA_FILTER_APPLY',		'Aplicar filtrado');
define('_MEDIA_FILTER_LABEL',		'Filtrado: ');
define('_MEDIA_UPLOAD_TO',			'Subir a...');
define('_MEDIA_UPLOAD_NEW',			'Subir novo arquivo...');
define('_MEDIA_COLLECTION_SELECT',	'Seleccionar');
define('_MEDIA_COLLECTION_TT',		'Cambiar a esta categoría');
define('_MEDIA_COLLECTION_LABEL',	'Colección actual: ');

// tooltips on toolbar
define('_ADD_ALIGNLEFT_TT',			'Aliñar á esquerda');
define('_ADD_ALIGNRIGHT_TT',		'Aliñar á dereita');
define('_ADD_ALIGNCENTER_TT',		'Aliñar no centro');


// generic upload failure
define('_ERROR_UPLOADFAILED',		'Erro na subida');

// END introduced after v2.0 END

// START introduced after v1.5 START

// posting to the past/edit timestamps
define('_EBLOG_ALLOWPASTPOSTING',	'Permitir publicar entradas en arquivos antigos');
define('_ADD_CHANGEDATE',			'Actualizar marcas de tempo');
define('_BMLET_CHANGEDATE',			'Actualizar marcas de tempo');

// skin import/export
define('_OVERVIEW_SKINIMPORT',		'Importar/exportar pel...');

// skin settings
define('_PARSER_INCMODE_NORMAL',	'Normal');
define('_PARSER_INCMODE_SKINDIR',	'Utilizar o directorio de peles');
define('_SKIN_INCLUDE_MODE',		'Incluír modo');
define('_SKIN_INCLUDE_PREFIX',		'Incluír prefixo');

// global settings
define('_SETTINGS_BASESKIN',		'Pel base');
define('_SETTINGS_SKINSURL',		'URL das peles');
define('_SETTINGS_ACTIONSURL',		'URL completa para a action.php');

// category moves (batch)
define('_ERROR_MOVEDEFCATEGORY',	'Imposible cambiar a categoría por defecto');
define('_ERROR_MOVETOSELF',			'Imposible cambiar categoría (a bitácora de destino é a mesma que a de orixe)');
define('_MOVECAT_TITLE',			'Selecciona a bitácora á que queres enviar esta categoría');
define('_MOVECAT_BTN',				'Cambiar categoría');

// URLMode setting
define('_SETTINGS_URLMODE',			'Modo URL');
define('_SETTINGS_URLMODE_NORMAL',	'Normal');
define('_SETTINGS_URLMODE_PATHINFO','Atractiva');

// Batch operations
define('_BATCH_NOSELECTION',		'Non se seleccionou algo sobre o que executar as accións');
define('_BATCH_ITEMS',				'Procesar por lotes os elementos');
define('_BATCH_CATEGORIES',			'Procesar por lotes as categorías');
define('_BATCH_MEMBERS',			'Procesar por lotes os membros');
define('_BATCH_TEAM',				'Procesar por lotes os membros dun equipo');
define('_BATCH_COMMENTS',			'Procesar por lotes os comentarios');
define('_BATCH_UNKNOWN',			'Procesamento por lotes descoñecido: ');
define('_BATCH_EXECUTING',			'Executando');
define('_BATCH_ONCATEGORY',			'na categoría');
define('_BATCH_ONITEM',				'no elemento');
define('_BATCH_ONCOMMENT',			'no comentario');
define('_BATCH_ONMEMBER',			'no membro');
define('_BATCH_ONTEAM',				'no membro do equipo');
define('_BATCH_SUCCESS',			'Realizado!');
define('_BATCH_DONE',				'Feito!');
define('_BATCH_DELETE_CONFIRM',		'Confirmar eliminación');
define('_BATCH_DELETE_CONFIRM_BTN',	'Confirmar eliminación');
define('_BATCH_SELECTALL',			'seleccionar todos');
define('_BATCH_DESELECTALL',		'desmarcar todos');

// batch operations: options in dropdowns
define('_BATCH_ITEM_DELETE',		'Eliminar');
define('_BATCH_ITEM_MOVE',			'Mover');
define('_BATCH_MEMBER_DELETE',		'Eliminar');
define('_BATCH_MEMBER_SET_ADM',		'Outorgar dereitos de administrador');
define('_BATCH_MEMBER_UNSET_ADM',	'Retirar dereitos de administrador');
define('_BATCH_TEAM_DELETE',		'Eliminar do equipo');
define('_BATCH_TEAM_SET_ADM',		'Proporcionar dereitos de administrador');
define('_BATCH_TEAM_UNSET_ADM',		'Retirar dereitos de administrador');
define('_BATCH_CAT_DELETE',			'Eliminar');
define('_BATCH_CAT_MOVE',			'Cambiar a outra bitácora');
define('_BATCH_COMMENT_DELETE',		'Eliminar');

// itemlist: Add new item...
define('_ITEMLIST_ADDNEW',			'Engadir un novo elemento...');
define('_ADD_PLUGIN_EXTRAS',		'Opcións extra das extensións');

// errors
define('_ERROR_CATCREATEFAIL',		'Imposible crear unha nova categoría');
define('_ERROR_NUCLEUSVERSIONREQ',	'Para esta extensión cómpre ter a seguinte versión de Nucleus: ');

// backlinks
define('_BACK_TO_BLOGSETTINGS',		'Volver á configuración da bitácora');

// skin import export
define('_SKINIE_TITLE_IMPORT',		'Importar');
define('_SKINIE_TITLE_EXPORT',		'Exportar');
define('_SKINIE_BTN_IMPORT',		'Importar');
define('_SKINIE_BTN_EXPORT',		'Exportar os patróns/peles seleccionadas');
define('_SKINIE_LOCAL',				'Importar dun arquivo local:');
define('_SKINIE_NOCANDIDATES',		'Non se localizaron elementos para importar no directorio de peles');
define('_SKINIE_FROMURL',			'Importar dunha URL:');
define('_SKINIE_EXPORT_INTRO',		'Selecciona abaixo as peles e patróns que queres exportar');
define('_SKINIE_EXPORT_SKINS',		'Peles');
define('_SKINIE_EXPORT_TEMPLATES',	'Patróns');
define('_SKINIE_EXPORT_EXTRA',		'Información extra');
define('_SKINIE_CONFIRM_OVERWRITE',	'Sobreescribir peles que xa existen (ver conflito entre nomes');
define('_SKINIE_CONFIRM_IMPORT',	'Si, quero importar esto');
define('_SKINIE_CONFIRM_TITLE',		'Acerca de importar peles e patróns');
define('_SKINIE_INFO_SKINS',		'Peles no arquivo:');
define('_SKINIE_INFO_TEMPLATES',	'Patróns no arquivo:');
define('_SKINIE_INFO_GENERAL',		'Información:');
define('_SKINIE_INFO_SKINCLASH',	'Conflito co nome da pel:');
define('_SKINIE_INFO_TEMPLCLASH',	'Conflito co nome do patrón:');
define('_SKINIE_INFO_IMPORTEDSKINS','Peles importadas:');
define('_SKINIE_INFO_IMPORTEDTEMPLS','Patróns importados:');
define('_SKINIE_DONE',				'Importación realizada');

define('_AND',						'e');
define('_OR',						'ou');

// empty fields on template edit
define('_EDITTEMPLATE_EMPTY',		'campo baleiro (preme para editar)');

// skin overview list
define('_LIST_SKINS_INCMODE',		'Incluír modo:');
define('_LIST_SKINS_INCPREFIX',		'Incluír prefixo:');
define('_LIST_SKINS_DEFINED',		'Partes definidas:');

// backup
define('_BACKUPS_TITLE',			'Copia / Restauración');
define('_BACKUP_TITLE',				'Copia');
define('_BACKUP_INTRO',				'Preme no botón de abaixo para crear unha copia da base de datos de Nucleus. Requeriráseche que gardes un arquivo coa copia. Gárdao nun lugar seguro.');
define('_BACKUP_ZIP_YES',			'Tenta comprimilo');
define('_BACKUP_ZIP_NO',			'Non o comprimas');
define('_BACKUP_BTN',				'Crear unha copia');
define('_BACKUP_NOTE',				'<b>Nota:</b>Tan só os contidos da base de datos son gardados na copia. Os arquivos multimedia e as preferencias de configuración en config.php <b>non</b> están por tanto incluídas na copia.');
define('_RESTORE_TITLE',			'Restaurar');
define('_RESTORE_NOTE',				'<b>Advertencia:</b> Restaurar dende unha copia <b>ELIMINARÁ</b> todos os datos que se atopen actualmente na base de datos de Nucleus! Realiza esta operación soamente cando esteas completamente seguro<br />	<b>Nota:</b>A versión de Nucleus na que creaches a copia debe ser a mesma que a que estás a usar agora. Asegúrate de que son iguais, xa que senón, non funcionará ');
define('_RESTORE_INTRO',			'Selecciona a copia debaixo (subirase ao servidor) e preme no botón "Restaurar" para comezar.');
define('_RESTORE_IMSURE',			'Si, estou seguro de que quero facer esto!');
define('_RESTORE_BTN',				'Restaurar dende arquivo');
define('_RESTORE_WARNING',			'(asegúrate de que estás a restaurar a copia correcta; cecais deberías facer unha nova copia antes de comezar)');
define('_ERROR_BACKUP_NOTSURE',		'Necesitas marcar a caixa de texto \'Estou seguro\'');
define('_RESTORE_COMPLETE',			'Restauración realizada');

// new item notification
define('_NOTIFY_NI_MSG',			'Foi publicado un novo elemento:');
define('_NOTIFY_NI_TITLE',			'Novo elemento!');
define('_NOTIFY_KV_MSG',			'Voto karma do elemento:');
define('_NOTIFY_KV_TITLE',			'Karma de Nucleus:');
define('_NOTIFY_NC_MSG',			'Comentario sobre o elemento:');
define('_NOTIFY_NC_TITLE',			'Comentario de Nucleus:');
define('_NOTIFY_USERID',			'ID de usuario:');
define('_NOTIFY_USER',				'Usuario:');
define('_NOTIFY_COMMENT',			'Comentario:');
define('_NOTIFY_VOTE',				'Voto:');
define('_NOTIFY_HOST',				'Host:');
define('_NOTIFY_IP',				'IP:');
define('_NOTIFY_MEMBER',			'Membro:');
define('_NOTIFY_TITLE',				'Título:');
define('_NOTIFY_CONTENTS',			'Contidos:');

// member mail message
define('_MMAIL_MSG',				'Mensaxe enviada por');
define('_MMAIL_FROMANON',			'visitante anónimo');
define('_MMAIL_FROMNUC',			'Publicado dende a bitácora de Nucleus');
define('_MMAIL_TITLE',				'Mensaxe de');
define('_MMAIL_MAIL',				'Mensaxe:');

// END introduced after v1.5 END


// START introduced after v1.1 START

// bookmarklet buttons
define('_BMLET_ADD',				'Engadir entrada');
define('_BMLET_EDIT',				'Editar entrada');
define('_BMLET_DELETE',				'Eliminar entrada');
define('_BMLET_BODY',				'Corpo');
define('_BMLET_MORE',				'Estendido');
define('_BMLET_OPTIONS',			'Opcións');
define('_BMLET_PREVIEW',			'Vista previa');

// used in bookmarklet
define('_ITEM_UPDATED',				'Actualizouse a entrada');
define('_ITEM_DELETED',				'Eliminouse a entrada');

// plugins
define('_CONFIRMTXT_PLUGIN',		'Estás seguro de que desexas eliminar a extensión');
define('_ERROR_NOSUCHPLUGIN',		'Esta extensión non existe');
define('_ERROR_DUPPLUGIN',			'Síntoo, esta extensión xa está instalada');
define('_ERROR_PLUGFILEERROR',		'Esta extensión non existe, ou os permisos están incorrectamente configurados');
define('_PLUGS_NOCANDIDATES',		'Non se localizaron extensións');

define('_PLUGS_TITLE_MANAGE',		'Administrar extensións');
define('_PLUGS_TITLE_INSTALLED',	'Instaladas actualmente');
define('_PLUGS_TITLE_UPDATE',		'Actualizar a lista de subscrición');
define('_PLUGS_TEXT_UPDATE',		'Nucleus garda na caché os datos relacionados coa subscrición das extensións. Cando actualizas unha extensión substituíndo o seu arquivo, debes comprobar que a subscrición queda rexistrada na caché');
define('_PLUGS_TITLE_NEW',			'Instalar unha nova extensión');
define('_PLUGS_ADD_TEXT',			'Debaixo podes ver unha lista de todos os arquivos no teu directorio de extensións, que posiblemente non son extensións susceptibles de ser instalables. Asegúrate de que se trata dunha extensión antes de instalala.');
define('_PLUGS_BTN_INSTALL',		'Instalar extensión');
define('_BACKTOOVERVIEW',			'Volver a vista xeral');

// editlink
define('_TEMPLATE_EDITLINK',		'Editar a ligazón da entrada');

// add left / add right tooltips
define('_ADD_LEFT_TT',				'Engadir cadro na esquerda');
define('_ADD_RIGHT_TT',				'Engadir cadro na dereita');

// add/edit item: new category (in dropdown box)
define('_ADD_NEWCAT',				'Nova categoría...');

// new settings
define('_SETTINGS_PLUGINURL',		'URL da extensión');
define('_SETTINGS_MAXUPLOADSIZE',	'Tamaño máximo dos arquivos a subir (bytes)');
define('_SETTINGS_NONMEMBERMSGS',	'Permitir aos usuarios non rexistrados enviar mensaxes');
define('_SETTINGS_PROTECTMEMNAMES',	'Protexer os nomes dos membros');

// overview screen
define('_OVERVIEW_PLUGINS',			'Xestionar extensións...');

// actionlog
define('_ACTIONLOG_NEWMEMBER',		'Subscrición dun novo membro:');

// membermail (when not logged in)
define('_MEMBERMAIL_MAIL',			'Correo-e:');

// file upload
define('_ERROR_DISALLOWEDUPLOAD2',	'Non posúes dereitos de administrador en ningunha das bitácoras <strong>que teñen o membro de destino na súa lista de equipos</strong>. Polo tanto, non che está permitido subir arquivos ao directorio multimedia deste membro');

// plugin list
define('_LISTS_INFO',				'Información');
define('_LIST_PLUGS_AUTHOR',		'Por:');
define('_LIST_PLUGS_VER',			'Versión:');
define('_LIST_PLUGS_SITE',			'Visitar o sitio');
define('_LIST_PLUGS_DESC',			'Descrición:');
define('_LIST_PLUGS_SUBS',			'Subscribiuse aos seguintes eventos:');
define('_LIST_PLUGS_UP',			'subir');
define('_LIST_PLUGS_DOWN',			'baixar');
define('_LIST_PLUGS_UNINSTALL',		'desinstalar');
define('_LIST_PLUGS_ADMIN',			'administrador');
define('_LIST_PLUGS_OPTIONS',		'editar&nbsp;opcións');

// plugin option list
define('_LISTS_VALUE',				'Valor');

// plugin options
define('_ERROR_NOPLUGOPTIONS',		'Esta extensión non ten configurada ningunha opción');
define('_PLUGS_BACK',				'Volver á vista xeral das extensións');
define('_PLUGS_SAVE',				'Gardar opcións');
define('_PLUGS_OPTIONS_UPDATED',	'Opción de extensións actualizadas');

define('_OVERVIEW_MANAGEMENT',		'Xestión');
define('_OVERVIEW_MANAGE',			'Xestión de Nucleus...');
define('_MANAGE_GENERAL',			'Xestión xeral');
define('_MANAGE_SKINS',				'Peles e patróns');
define('_MANAGE_EXTRA',				'Características extra');

define('_BACKTOMANAGE',				'Volver a xestión de Nucleus');


// END introduced after v1.1 END




// charset to use
define('_CHARSET',					'iso-8859-1');

// global stuff
define('_LOGOUT',					'Pechar sesión');
define('_LOGIN',					'Rexistrar');
define('_YES',						'Si');
define('_NO',						'Non');
define('_SUBMIT',					'Enviar');
define('_ERROR',					'Erro');
define('_ERRORMSG',					'Produciuse un erro!');
define('_BACK',						'Volver');
define('_NOTLOGGEDIN',				'Sesión non iniciada');
define('_LOGGEDINAS',				'Sesión iniciada como');
define('_ADMINHOME',				'Inicio (administrador)');
define('_NAME',						'Nome');
define('_BACKHOME',					'Volver ao inicio (administrador)');
define('_BADACTION',				'A acción solicitada non existe');
define('_MESSAGE',					'Mensaxe');
define('_HELP_TT',					'Axuda!');
define('_YOURSITE',					'A túa bitácora');


define('_POPUP_CLOSE',				'Pechar ventá');

define('_LOGIN_PLEASE',				'Por favor, inicia a sesión');

// commentform
define('_COMMENTFORM_YOUARE',		'Ti es');
define('_COMMENTFORM_SUBMIT',		'Engadir comentario');
define('_COMMENTFORM_COMMENT',		'O teu comentario');
define('_COMMENTFORM_NAME',			'Nome');
define('_COMMENTFORM_MAIL',			'Correo-e/HTTP');
define('_COMMENTFORM_REMEMBER',		'Lémbrame');

// loginform
define('_LOGINFORM_NAME',			'Nome de usuario');
define('_LOGINFORM_PWD',			'Contrasinal');
define('_LOGINFORM_YOUARE',			'Sesión iniciada como');
define('_LOGINFORM_SHARED',			'Ordenador compartido');

// member mailform
define('_MEMBERMAIL_SUBMIT',		'Enviar mensaxe');

// search form
define('_SEARCHFORM_SUBMIT',		'Procurar');

// add item form
define('_ADD_ADDTO',				'Engadir nova entrada en');
define('_ADD_CREATENEW',			'Crear nova entrada');
define('_ADD_BODY',					'Corpo');
define('_ADD_TITLE',				'Título');
define('_ADD_MORE',					'Estendido (opcional)');
define('_ADD_CATEGORY',				'Categoría');
define('_ADD_PREVIEW',				'Vista previa');
define('_ADD_DISABLE_COMMENTS',		'Deshabilitar comentarios?');
define('_ADD_DRAFTNFUTURE',			'Borrador e futuras entradas');
define('_ADD_ADDITEM',				'Engadir entrada');
define('_ADD_ADDNOW',				'Engadir agora');
define('_ADD_ADDLATER',				'Engadir logo');
define('_ADD_PLACE_ON',				'Colocar');
define('_ADD_ADDDRAFT',				'Engadir a borradores');
define('_ADD_NOPASTDATES',			'(as datas e horas do pasado non son válidas, a hora actual será empregada neste caso)');
define('_ADD_BOLD_TT',				'Negra');
define('_ADD_ITALIC_TT',			'Cursiva');
define('_ADD_HREF_TT',				'Crear ligazón');
define('_ADD_MEDIA_TT',				'Engadir recurso multimedia');
define('_ADD_PREVIEW_TT',			'Mostrar/ocultar vista previa');
define('_ADD_CUT_TT',				'Cortar');
define('_ADD_COPY_TT',				'Copiar');
define('_ADD_PASTE_TT',				'Pegar');


// edit item form
define('_EDIT_ITEM',				'Editar entrada');
define('_EDIT_SUBMIT',				'Editar entrada');
define('_EDIT_ORIG_AUTHOR',			'Autor orixinal');
define('_EDIT_BACKTODRAFTS',		'Engadir resposta aos borradores');
define('_EDIT_COMMENTSNOTE',		'(nota: a deshabilitación de comentarios non ocultará os comentarios previamente engadidos)');

// used on delete screens
define('_DELETE_CONFIRM',			'Por favor, confirma a eliminación');
define('_DELETE_CONFIRM_BTN',		'Confirmar eliminación');
define('_CONFIRMTXT_ITEM',			'Estás a piques de eliminar esta entrada:');
define('_CONFIRMTXT_COMMENT',		'Estás a pique de eliminar os seguintes comentarios:');
define('_CONFIRMTXT_TEAM1',			'Estás a pique de eliminar ');
define('_CONFIRMTXT_TEAM2',			' da lista de grupos da bitácora ');
define('_CONFIRMTXT_BLOG',			'A bitácora que queres eliminar é: ');
define('_WARNINGTXT_BLOGDEL',		'Advertencia! A eliminación dunha bitácora supón a eliminación de todas as entradas e comentarios desa bitácora. Por favor, confirma que queres eliminala<br />Non interrumpas a Nucleus  mentres está a eliminar a túa bitácora.');
define('_CONFIRMTXT_MEMBER',		'Estás a piques de eliminar o perfil do seguinte membro: ');
define('_CONFIRMTXT_TEMPLATE',		'Estás a piques de eliminar o patrón ');
define('_CONFIRMTXT_SKIN',			'Estás a piques de eliminar a pel ');
define('_CONFIRMTXT_BAN',			'Estás a piques de eliminar a restricción para o rango de IP');
define('_CONFIRMTXT_CATEGORY',		'Estás a piques de eliminar a categoría');

// some status messages
define('_DELETED_ITEM',				'Entrada eliminada');
define('_DELETED_MEMBER',			'Membro eliminado');
define('_DELETED_COMMENT',			'Comentario eliminado');
define('_DELETED_BLOG',				'Bitácora eliminada');
define('_DELETED_CATEGORY',			'Categoría eliminada');
define('_ITEM_MOVED',				'Entrada cambiada');
define('_ITEM_ADDED',				'Entrada engadida');
define('_COMMENT_UPDATED',			'Comentario actualizado');
define('_SKIN_UPDATED',				'Os datos da pel foron gardados');
define('_TEMPLATE_UPDATED',			'Os datos do patrón foron gardados');

// errors
define('_ERROR_COMMENT_LONGWORD',	'Por favor, non empregues palabras dunha lonxitude superior a 90 nos teus comentarios');
define('_ERROR_COMMENT_NOCOMMENT',	'Por favor, introduce un comentario');
define('_ERROR_COMMENT_NOUSERNAME',	'Usuario incorrecto');
define('_ERROR_COMMENT_TOOLONG',	'Os teus comentarios son demasiado longos (max. 5000 carac.)');
define('_ERROR_COMMENTS_DISABLED',	'Os comentarios para esta bitácora están actualmente deshabilitados.');
define('_ERROR_COMMENTS_NONPUBLIC',	'Debes estar rexistrado como usuario para engadir comentarios a esta bitácora');
define('_ERROR_COMMENTS_MEMBERNICK','O nome que queres empregar para publicar comentarios xa se encontra en uso. Escolle outro.');
define('_ERROR_SKIN',				'Erro na pel');
define('_ERROR_ITEMCLOSED',			'Esta entrada está pechada, non é posible engadir novos comentarios nin votar');
define('_ERROR_NOSUCHITEM',			'A entrada indicada non existe');
define('_ERROR_NOSUCHBLOG',			'A bitácora indicada non existe');
define('_ERROR_NOSUCHSKIN',			'A pel indicada non existe');
define('_ERROR_NOSUCHMEMBER',		'O membro indicado non existe');
define('_ERROR_NOTONTEAM',			'Non estás entre o equipo de usuarios deste bitácora.');
define('_ERROR_BADDESTBLOG',		'A bitácora de destino non existe');
define('_ERROR_NOTONDESTTEAM',		'Imposible cambiar a entrada, xa que non eres membro do equipo de usuarios da bitácora de destino');
define('_ERROR_NOEMPTYITEMS',		'Imposible introducir entradas baleiras!');
define('_ERROR_BADMAILADDRESS',		'Dirección de correo-e incorrecta');
define('_ERROR_BADNOTIFY',			'Unha ou varias das direccións de notificación non é válida');
define('_ERROR_BADNAME',			'Nome incorrecto (só se permite letras da a-z e números do 0-9, sen espazos no comezo/fin)');
define('_ERROR_NICKNAMEINUSE',		'Xa existe outro membro que está a empregar o mesmo alcume');
define('_ERROR_PASSWORDMISMATCH',	'Os contrasinais deben coincidir');
define('_ERROR_PASSWORDTOOSHORT',	'O contrasinal debe incluír cando menos 6 caracteres');
define('_ERROR_PASSWORDMISSING',	'O contrasinal non pode quedar baleiro');
define('_ERROR_REALNAMEMISSING',	'Debes introducir un nome real');
define('_ERROR_ATLEASTONEADMIN',	'Sempre debería existir un superadministrador que puidese iniciar sesión na área de administración.');
define('_ERROR_ATLEASTONEBLOGADMIN','A realización desta acción  deixará a túa bitácora inoperativa. Por favor, asegúrate de que sempre existe alomenos un administrador.');
define('_ERROR_ALREADYONTEAM',		'Non podes engadir un membro que xa forma parte do equipo');
define('_ERROR_BADSHORTBLOGNAME',	'O nome curto da bitácora só debe conter letras da a-z e números do 0-9, sen espazos');
define('_ERROR_DUPSHORTBLOGNAME',	'Xa existe outra bitácora co nome curto seleccionado. Estos nomes deben ser únicos');
define('_ERROR_UPDATEFILE',			'Non tes permiso de escritura para actualizar o arquivo. Asegúrate de que os permisos para os arquivos están correctamente configurados (en Unix/linux proba con chmod 666; en Windows verifica se o arquivo é de só lectura). A localización debe ser relativa ao directorio de administración, polo que sería recomendable o uso dunha ruta absoluta (velaquí un exemplo/camiño/ata/nucleus/)');
define('_ERROR_DELDEFBLOG',			'Imposible eliminar a bitácora por defecto');
define('_ERROR_DELETEMEMBER',		'Imposible eliminar este membro, probablemente porque é autor de entradas ou comentarios');
define('_ERROR_BADTEMPLATENAME',	'Nome de patrón incorrecto, usa só palabras da a-z e números do 0-9, sen espazos');
define('_ERROR_DUPTEMPLATENAME',	'Xa existe un patrón co mesmo nome');
define('_ERROR_BADSKINNAME',		'Nome para a pel incorrecto (só se permiten letras da a-z, e números do 0-9, sen espazos)');
define('_ERROR_DUPSKINNAME',		'Xa existe outra pel co mesmo nome');
define('_ERROR_DEFAULTSKIN',		'Sempre debe existir unha pel chamada "default"');
define('_ERROR_SKINDEFDELETE',		'Imposible eliminar a pel, xa que é a pel por defecto da seguinte bitácora: ');
define('_ERROR_DISALLOWED',			'Síntoo, non tes permiso para realizar esta acción');
define('_ERROR_DELETEBAN',			'Erro na eliminación da restricción (a restricción non existe)');
define('_ERROR_ADDBAN',				'Erro na introdución da restricción. É posible que a restricción non teña sido engadida correctamente en todas as túas bitácoras.');
define('_ERROR_BADACTION',			'A acción requerida non existe');
define('_ERROR_MEMBERMAILDISABLED',	'O envío de mensaxes entre membros está deshabilitado');
define('_ERROR_MEMBERCREATEDISABLED','A creación de contas de membro está deshabilitada');
define('_ERROR_INCORRECTEMAIL',		'Dirección de correo-e incorrecta');
define('_ERROR_VOTEDBEFORE',		'Xa votaches nesta entrada');
define('_ERROR_BANNED1',			'Imposible realizar esta acción (rango de IP ');
define('_ERROR_BANNED2',			') xa que tes unha restricción. A mensaxe era: \'');
define('_ERROR_BANNED3',			'\'');
define('_ERROR_LOGINNEEDED',		'Debes ter iniciada a sesión para realizar esta acción');
define('_ERROR_CONNECT',			'Erro de conexión');
define('_ERROR_FILE_TOO_BIG',		'O arquivo é demasiado grande!');
define('_ERROR_BADFILETYPE',		'Síntoo, este tipo de arquivo non está permitido');
define('_ERROR_BADREQUEST',			'Erro no envío de arquivo');
define('_ERROR_DISALLOWEDUPLOAD',	'Non formas parte do equipo dunha bitácora. En consecuencia, non podes enviar arquivos');
define('_ERROR_BADPERMISSIONS',		'Os permisos para o arquivo/directorio non están correctamente configurados');
define('_ERROR_UPLOADMOVEP',		'Erro no cambio do arquivo enviado');
define('_ERROR_UPLOADCOPY',			'Erro na copia do arquivo');
define('_ERROR_UPLOADDUPLICATE',	'Xa existe outro arquivo co mesmo nome. Indica outro nome antes de enviar.');
define('_ERROR_LOGINDISALLOWED',	'Síntoo, non podes iniciar sesión na área de administración. Podes iniciar sesión como outro usuario');
define('_ERROR_DBCONNECT',			'Imposible conectar co meu servidor MySQL');
define('_ERROR_DBSELECT',			'Imposible seleccionar a base de datos de Nucleus.');
define('_ERROR_NOSUCHLANGUAGE',		'No existe tal arquivo de idioma');
define('_ERROR_NOSUCHCATEGORY',		'Non existe tal categoría');
define('_ERROR_DELETELASTCATEGORY',	'Cando menos, debe existir unha categoría');
define('_ERROR_DELETEDEFCATEGORY',	'Non se poden eliminar as categorías por defecto');
define('_ERROR_BADCATEGORYNAME',	'Nome de categoría incorrecto');
define('_ERROR_DUPCATEGORYNAME',	'Xa existe outra categoría co mesmo nome');

// some warnings (used for mediadir setting)
define('_WARNING_NOTADIR',			'Advertencia: o valor actual non é un directorio!');
define('_WARNING_NOTREADABLE',		'Advertencia: o valor actual é un directorio sen permiso de lectura!');
define('_WARNING_NOTWRITABLE',		'Advertencia: o valor actual non é un directorio con permiso de escritura!');

// media and upload
define('_MEDIA_UPLOADLINK',			'Enviar novos arquivos');
define('_MEDIA_MODIFIED',			'modificado');
define('_MEDIA_FILENAME',			'nome do arquivo');
define('_MEDIA_DIMENSIONS',			'dimensións');
define('_MEDIA_INLINE',				'Elementos en liña');
define('_MEDIA_POPUP',				'Ventá emerxente');
define('_UPLOAD_TITLE',				'Escolle un arquivo');
define('_UPLOAD_MSG',				'Escolle o arquivo que queres enviar, e preme no botón \'Enviar\'.');
define('_UPLOAD_BUTTON',			'Enviar');

// some status messages
define('_MSG_ACCOUNTCREATED',		'Conta creada; o contrasinal será enviado por correo-e');
define('_MSG_PASSWORDSENT',			'Enviouse o contrasinal por correo-e.');
define('_MSG_LOGINAGAIN',			'Debes reiniciar a sesión, xa que os teus datos de usuario foron modificados');
define('_MSG_SETTINGSCHANGED',		'Preferencias modificadas');
define('_MSG_ADMINCHANGED',			'Administrador modificado');
define('_MSG_NEWBLOG',				'Nova bitácora creada');
define('_MSG_ACTIONLOGCLEARED',		'Rexistro de actividades limpo');

// actionlog in admin area
define('_ACTIONLOG_DISALLOWED',		'Acción non permitida: ');
define('_ACTIONLOG_PWDREMINDERSENT','Enviouse novo contrasinal a ');
define('_ACTIONLOG_TITLE',			'Rexistro de actividades');
define('_ACTIONLOG_CLEAR_TITLE',	'Limpar o rexistro de actividades');
define('_ACTIONLOG_CLEAR_TEXT',		'Limpar o rexistro de actividades agora');

// team management
define('_TEAM_TITLE',				'Xestionar o equipo da bitácora');
define('_TEAM_CURRENT',				'Equipo actual');
define('_TEAM_ADDNEW',				'Engadir novo membro ao equipo');
define('_TEAM_CHOOSEMEMBER',		'Selecciona un membro');
define('_TEAM_ADMIN',				'Privilexios de administrador? ');
define('_TEAM_ADD',					'Engadir ao equipo');
define('_TEAM_ADD_BTN',				'Engadir ao equipo');

// blogsettings
define('_EBLOG_TITLE',				'Editar preferencias da bitácora');
define('_EBLOG_TEAM_TITLE',			'Editar o equipo');
define('_EBLOG_TEAM_TEXT',			'Preme aquí para editar o teu equipo...');
define('_EBLOG_SETTINGS_TITLE',		'Preferencias da bitácora');
define('_EBLOG_NAME',				'Nome da bitácora');
define('_EBLOG_SHORTNAME',			'Nome curto da bitácora');
define('_EBLOG_SHORTNAME_EXTRA',	'<br />(só debe conter letras da a-z e non ter espazos)');
define('_EBLOG_DESC',				'Descrición da bitácora');
define('_EBLOG_URL',				'URL');
define('_EBLOG_DEFSKIN',			'Pel por defecto');
define('_EBLOG_DEFCAT',				'Categoría por defecto');
define('_EBLOG_LINEBREAKS',			'Converter saltos de liña');
define('_EBLOG_DISABLECOMMENTS',	'Habilitar comentarios?<br /><small>(Deshabilitar os comentarios significa que non é posible engadir comentarios.)</small>');
define('_EBLOG_ANONYMOUS',			'Permitir comentarios de usarios que non son membros?');
define('_EBLOG_NOTIFY',				'Dirección(s) para a notificación (usa ; como separador)');
define('_EBLOG_NOTIFY_ON',			'Notificar a');
define('_EBLOG_NOTIFY_COMMENT',		'Novos comentarios');
define('_EBLOG_NOTIFY_KARMA',		'Novos votos');
define('_EBLOG_NOTIFY_ITEM',		'Novas entradas');
define('_EBLOG_PING',				'Facer ping a Weblogs.com ao actualizar?');
define('_EBLOG_MAXCOMMENTS',		'Cantidade máxima de comentarios');
define('_EBLOG_UPDATE',				'Actualizar arquivo');
define('_EBLOG_OFFSET',				'Zona horaria');
define('_EBLOG_STIME',				'Hora actual do servidor');
define('_EBLOG_BTIME',				'Hora actual da bitácora');
define('_EBLOG_CHANGE',				'Cambiar preferencias');
define('_EBLOG_CHANGE_BTN',			'Cambiar preferencias');
define('_EBLOG_ADMIN',				'Administrador da bitácora');
define('_EBLOG_ADMIN_MSG',			'Asignaránseche privilexios de administrador');
define('_EBLOG_CREATE_TITLE',		'Crear nova bitácora');
define('_EBLOG_CREATE_TEXT',		'Completa o seguinte formulario para crear unha nova bitácora. <br /><br /> <b>Nota:</b> Só aparecen listadas as opcións necesarias. Para configurar opcións extra, entra nas preferencias da bitácora unha vez creada.');
define('_EBLOG_CREATE',				'Crear!');
define('_EBLOG_CREATE_BTN',			'Crear unha bitácora');
define('_EBLOG_CAT_TITLE',			'Categorías');
define('_EBLOG_CAT_NAME',			'Nome da categoría');
define('_EBLOG_CAT_DESC',			'Descrición da categoría');
define('_EBLOG_CAT_CREATE',			'Crear nova categoría');
define('_EBLOG_CAT_UPDATE',			'Actualizar categoría');
define('_EBLOG_CAT_UPDATE_BTN',		'Actualizar categoría');

// templates
define('_TEMPLATE_TITLE',			'Editar patróns');
define('_TEMPLATE_AVAILABLE_TITLE',	'Patróns dispoñibles');
define('_TEMPLATE_NEW_TITLE',		'Novo patrón');
define('_TEMPLATE_NAME',			'Nome do patrón');
define('_TEMPLATE_DESC',			'Descrición do patrón');
define('_TEMPLATE_CREATE',			'Crear patrón');
define('_TEMPLATE_CREATE_BTN',		'Crear patrón');
define('_TEMPLATE_EDIT_TITLE',		'Editar patrón');
define('_TEMPLATE_BACK',			'Volver á vista xeral dos patróns');
define('_TEMPLATE_EDIT_MSG',		'Non todas as partes do patrón son necesarias, deixa baleiras aquelas que non necesites.');
define('_TEMPLATE_SETTINGS',		'Preferencias dos patróns');
define('_TEMPLATE_ITEMS',			'Entradas');
define('_TEMPLATE_ITEMHEADER',		'Cabeceira da entrada');
define('_TEMPLATE_ITEMBODY',		'Corpo da entrada');
define('_TEMPLATE_ITEMFOOTER',		'Pé da entrada');
define('_TEMPLATE_MORELINK',		'Ligazón á extensión da entrada');
define('_TEMPLATE_NEW',				'Notificación de nova entrada');
define('_TEMPLATE_COMMENTS_ANY',	'Comentarios (se os hai)');
define('_TEMPLATE_CHEADER',			'Cabeceira dos comentarios');
define('_TEMPLATE_CBODY',			'Corpo dos comentarios');
define('_TEMPLATE_CFOOTER',			'Pé dos comentarios');
define('_TEMPLATE_CONE',			'Un comentario');
define('_TEMPLATE_CMANY',			'Dous (ou máis) comentarios');
define('_TEMPLATE_CMORE',			'Comentarios Ler máis');
define('_TEMPLATE_CMEXTRA',			'Membro extra');
define('_TEMPLATE_COMMENTS_NONE',	'Comentarios(se non hai)');
define('_TEMPLATE_CNONE',			'Non hai comentarios');
define('_TEMPLATE_COMMENTS_TOOMUCH','Comentarios (se os hai, pero son demasiados para amosar directamente)');
define('_TEMPLATE_CTOOMUCH',		'Demasiados comentarios');
define('_TEMPLATE_ARCHIVELIST',		'Listas de arquivos');
define('_TEMPLATE_AHEADER',			'Cabeceira da lista de arquivos');
define('_TEMPLATE_AITEM',			'Elemento da lista de arquivos');
define('_TEMPLATE_AFOOTER',			'Pé da lista de arquivos');
define('_TEMPLATE_DATETIME',		'Data e hora');
define('_TEMPLATE_DHEADER',			'Cabeceira da data');
define('_TEMPLATE_DFOOTER',			'Pé da data');
define('_TEMPLATE_DFORMAT',			'Formato da data');
define('_TEMPLATE_TFORMAT',			'Formato da hora');
define('_TEMPLATE_LOCALE',			'Local');
define('_TEMPLATE_IMAGE',			'Ventás de imaxes');
define('_TEMPLATE_PCODE',			'Código de ligazón a ventá emerxente');
define('_TEMPLATE_ICODE',			'Código de imaxe inserida');
define('_TEMPLATE_MCODE',			'Código de ligazón a elemento multimedia');
define('_TEMPLATE_SEARCH',			'Procurar');
define('_TEMPLATE_SHIGHLIGHT',		'Resaltar');
define('_TEMPLATE_SNOTFOUND',		'Non se atoparon resultados na procura');
define('_TEMPLATE_UPDATE',			'Actualizar');
define('_TEMPLATE_UPDATE_BTN',		'Actualizar patrón');
define('_TEMPLATE_RESET_BTN',		'Restablecer datos');
define('_TEMPLATE_CATEGORYLIST',	'Lista de categorías');
define('_TEMPLATE_CATHEADER',		'Cabeceira da lista de categorías');
define('_TEMPLATE_CATITEM',			'Elemento da lista de categorías');
define('_TEMPLATE_CATFOOTER',		'Pé da lista de categorías');

// skins
define('_SKIN_EDIT_TITLE',			'Editar peles');
define('_SKIN_AVAILABLE_TITLE',		'Peles dispoñibles');
define('_SKIN_NEW_TITLE',			'Nova pel');
define('_SKIN_NAME',				'Nome');
define('_SKIN_DESC',				'Descrición');
define('_SKIN_TYPE',				'Tipo de contido');
define('_SKIN_CREATE',				'Crear');
define('_SKIN_CREATE_BTN',			'Crear pel');
define('_SKIN_EDITONE_TITLE',		'Editar pel');
define('_SKIN_BACK',				'Volver á páxina principal da pel');
define('_SKIN_PARTS_TITLE',			'Partes da pel');
define('_SKIN_PARTS_MSG',			'Non todos os tipos son necesarios para cada pel. Deixa baleiros aqueles que non necesites. Escolle o tipo de pel que queres modificar:');
define('_SKIN_PART_MAIN',			'Índice principal');
define('_SKIN_PART_ITEM',			'Páxinas do elemento');
define('_SKIN_PART_ALIST',			'Lista de arquivos');
define('_SKIN_PART_ARCHIVE',		'Arquivo');
define('_SKIN_PART_SEARCH',			'Procurar');
define('_SKIN_PART_ERROR',			'Erros');
define('_SKIN_PART_MEMBER',			'Detalles dos membros');
define('_SKIN_PART_POPUP',			'Imaxes das ventás emerxentes');
define('_SKIN_GENSETTINGS_TITLE',	'Preferencias xerais');
define('_SKIN_CHANGE',				'Cambiar');
define('_SKIN_CHANGE_BTN',			'Cambiar estas preferencias');
define('_SKIN_UPDATE_BTN',			'Actualizar pel');
define('_SKIN_RESET_BTN',			'Restablecer os datos');
define('_SKIN_EDITPART_TITLE',		'Editar pel');
define('_SKIN_GOBACK',				'Volver');
define('_SKIN_ALLOWEDVARS',			'Variables permitidas (preme para obter máis información):');

// global settings
define('_SETTINGS_TITLE',			'Preferencias xerais');
define('_SETTINGS_SUB_GENERAL',		'Preferencias xerais');
define('_SETTINGS_DEFBLOG',			'Bitácora por defecto');
define('_SETTINGS_ADMINMAIL',		'Correo-e do administrador');
define('_SETTINGS_SITENAME',		'Nome do sitio web');
define('_SETTINGS_SITEURL',			'URL do sitio web (debe rematar cunha barra /)');
define('_SETTINGS_ADMINURL',		'URL da área de administración (debe rematar cunha barra /)');
define('_SETTINGS_DIRS',			'Directorios de Nucleus');
define('_SETTINGS_MEDIADIR',		'Directorio multimedia');
define('_SETTINGS_SEECONFIGPHP',	'(ver config.php)');
define('_SETTINGS_MEDIAURL',		'URL para elementos multimedia (debe rematar cunha barra /)');
define('_SETTINGS_ALLOWUPLOAD',		'Permitir o envío de arquivos?');
define('_SETTINGS_ALLOWUPLOADTYPES','Tipos de arquivos que se poden enviar');
define('_SETTINGS_CHANGELOGIN',		'Permitir aos membros cambiar os seus datos de rexistro/contrasinal');
define('_SETTINGS_COOKIES_TITLE',	'Preferencias das "cookies"');
define('_SETTINGS_COOKIELIFE',		'Duración da "galleta" de inicio de sesión');
define('_SETTINGS_COOKIESESSION',	'"Galletas" da sesión');
define('_SETTINGS_COOKIEMONTH',		'Duración de un mes');
define('_SETTINGS_COOKIEPATH',		'Camiño das "galletas" (avanzado)');
define('_SETTINGS_COOKIEDOMAIN',	'Dominio das "galletas" (avanzado)');
define('_SETTINGS_COOKIESECURE',	'"Galletas" seguras (avanzado)');
define('_SETTINGS_LASTVISIT',		'Gardar as "cookies" da derradeira visita');
define('_SETTINGS_ALLOWCREATE',		'Permitirlle aos visitantes crear unha conta de membro');
define('_SETTINGS_NEWLOGIN',		'Inicio de sesión permitido para contas creadas polos usuarios');
define('_SETTINGS_NEWLOGIN2',		'(só para contas creadas recentemente)');
define('_SETTINGS_MEMBERMSGS',		'Permitir os servizos membro a membro');
define('_SETTINGS_LANGUAGE',		'Idioma por defecto');
define('_SETTINGS_DISABLESITE',		'Deshabilitar sitio web');
define('_SETTINGS_DBLOGIN',			' Rexistro e base de datos MySQL');
define('_SETTINGS_UPDATE',			'Actualizar preferencias');
define('_SETTINGS_UPDATE_BTN',		'Actualizar preferencias');
define('_SETTINGS_DISABLEJS',		'Deshabilitar a barra de ferramentas JavaScript');
define('_SETTINGS_MEDIA',			'Preferencias de envío de elementos multimedia');
define('_SETTINGS_MEDIAPREFIX',		'Prefixar os arquivos enviados coa data');
define('_SETTINGS_MEMBERS',			'Preferencias dos membros');

// bans
define('_BAN_TITLE',				'Lista de restriccións para');
define('_BAN_NONE',					'Esta bitácora non ten restriccións');
define('_BAN_NEW_TITLE',			'Engadir nova restricción');
define('_BAN_NEW_TEXT',				'Engadir uha nova restricción agora');
define('_BAN_REMOVE_TITLE',			'Eliminar restricción');
define('_BAN_IPRANGE',				'Rango de IP');
define('_BAN_BLOGS',				'Que bitácoras?');
define('_BAN_DELETE_TITLE',			'Eliminar restricción');
define('_BAN_ALLBLOGS',				'Bitácoras nas que posúes dereitos de administrador.');
define('_BAN_REMOVED_TITLE',		'Restricción eliminada');
define('_BAN_REMOVED_TEXT',			'Eliminouse a restricción para as seguintes bitácoras:');
define('_BAN_ADD_TITLE',			'Engadir restricción');
define('_BAN_IPRANGE_TEXT',			'Escolle o rango IP que queres restrinxir debaixo. A menor cantidade de números, maior cantidade de direccións restrinxidas.');
define('_BAN_BLOGS_TEXT',			'Podes escoller entre restrinxir unha IP nunha única bitácora, ou restrinxila en todas as bitácoras nas que tes dereitos de administrador. Fai a túa selección debaixo.');
define('_BAN_REASON_TITLE',			'Razón');
define('_BAN_REASON_TEXT',			'Podes proporcionar unha razón para a restricción, que se mostrará cando o usuario con esa IP intente engadir un comentario ou votar. A lonxitude máxima é de 256 caracteres.');
define('_BAN_ADD_BTN',				'Engadir restricción');

// LOGIN screen
define('_LOGIN_MESSAGE',			'Mensaxe');
define('_LOGIN_NAME',				'Nome');
define('_LOGIN_PASSWORD',			'Contrasinal');
define('_LOGIN_SHARED',				_LOGINFORM_SHARED);
define('_LOGIN_FORGOT',				'Non te lembras do teu contrasinal?');

// membermanagement
define('_MEMBERS_TITLE',			'Xestión dos membros');
define('_MEMBERS_CURRENT',			'Membros actuais');
define('_MEMBERS_NEW',				'Novo membro');
define('_MEMBERS_DISPLAY',			'Nome público');
define('_MEMBERS_DISPLAY_INFO',		'(Este é o nome que empregas para iniciar sesión)');
define('_MEMBERS_REALNAME',			'Nome real');
define('_MEMBERS_PWD',				'Contrasinal');
define('_MEMBERS_REPPWD',			'Repite o contrasinal');
define('_MEMBERS_EMAIL',			'Dirección de correo-e');
define('_MEMBERS_EMAIL_EDIT',		'(Cando cambias a dirección de correo-e, automaticamente recibes o novo contrasinal na nova dirección de correo-e)');
define('_MEMBERS_URL',				'Dirección da web (URL)');
define('_MEMBERS_SUPERADMIN',		'Privilexios de administrador');
define('_MEMBERS_CANLOGIN',			'Podes acceder á área de administración');
define('_MEMBERS_NOTES',			'Notas');
define('_MEMBERS_NEW_BTN',			'Engadir membro');
define('_MEMBERS_EDIT',				'Editar membro');
define('_MEMBERS_EDIT_BTN',			'Modificar preferencias');
define('_MEMBERS_BACKTOOVERVIEW',	'Volver á páxina xeral de membros');
define('_MEMBERS_DEFLANG',			'Idioma');
define('_MEMBERS_USESITELANG',		'- usar as preferencias da web -');

// List of blogs (TT = tooltip)
define('_BLOGLIST_TT_VISIT',		'Visitar o sitio web');
define('_BLOGLIST_ADD',				'Engadir entrada');
define('_BLOGLIST_TT_ADD',			'Engadir unha nova entrada nesta bitácora');
define('_BLOGLIST_EDIT',			'Editar/Eliminar entradas');
define('_BLOGLIST_TT_EDIT',			'');
define('_BLOGLIST_BMLET',			'Marcador');
define('_BLOGLIST_TT_BMLET',		'');
define('_BLOGLIST_SETTINGS',		'Preferencias');
define('_BLOGLIST_TT_SETTINGS',		'Editar preferencias ou xestionar equipos');
define('_BLOGLIST_BANS',			'Restriccións');
define('_BLOGLIST_TT_BANS',			'Ver, engadir ou eliminar IPs restrinxidas');
define('_BLOGLIST_DELETE',			'Eliminar todo');
define('_BLOGLIST_TT_DELETE',		'Eliminar esta bitácora');

// OVERVIEW screen
define('_OVERVIEW_YRBLOGS',			'As túas bitácoras');
define('_OVERVIEW_YRDRAFTS',		'Os teus borradores');
define('_OVERVIEW_YRSETTINGS',		'As túas preferencias');
define('_OVERVIEW_GSETTINGS',		'Preferencias xerais');
define('_OVERVIEW_NOBLOGS',			'Non formas parte dun equipo de bitácora');
define('_OVERVIEW_NODRAFTS',		'Non hai borradores');
define('_OVERVIEW_EDITSETTINGS',	'Editar as túas preferencias...');
define('_OVERVIEW_BROWSEITEMS',		'Examinar as túas entradas...');
define('_OVERVIEW_BROWSECOMM',		'Examinar os teus comentarios...');
define('_OVERVIEW_VIEWLOG',			'Ver o rexistro de actividades...');
define('_OVERVIEW_MEMBERS',			'Xestionar membros...');
define('_OVERVIEW_NEWLOG',			'Crear nova bitácora...');
define('_OVERVIEW_SETTINGS',		'Editar preferencias...'); 
define('_OVERVIEW_TEMPLATES',		'Editar patróns...'); 
define('_OVERVIEW_SKINS',			'Editar peles...');
define('_OVERVIEW_BACKUP',			'Copia de seguridade/Restauración...');

// ITEMLIST
define('_ITEMLIST_BLOG',			'Entradas da bitácora');
define('_ITEMLIST_YOUR',			'As túas entradas');

// Comments
define('_COMMENTS',					'Comentarios');
define('_NOCOMMENTS',				'Esta entrada non ten comentarios');
define('_COMMENTS_YOUR',			'Os teus comentarios');
define('_NOCOMMENTS_YOUR',			'Non escribiches ningún comentario');

// LISTS (general)
define('_LISTS_NOMORE',				'No hai máis resultados, ou non hai ningún resultado');
define('_LISTS_PREV',				'Anterior');
define('_LISTS_NEXT',				'Seguinte');
define('_LISTS_SEARCH',				'Procurar');
define('_LISTS_CHANGE',				'Cambiar');
define('_LISTS_PERPAGE',			'entradas por páxina');
define('_LISTS_ACTIONS',			'Accións');
define('_LISTS_DELETE',				'Eliminar');
define('_LISTS_EDIT',				'Editar');
define('_LISTS_MOVE',				'Mover');
define('_LISTS_CLONE',				'Clonar');
define('_LISTS_TITLE',				'Título');
define('_LISTS_BLOG',				'Bitácora');
define('_LISTS_NAME',				'Nome');
define('_LISTS_DESC',				'Descrición');
define('_LISTS_TIME',				'Tempo');
define('_LISTS_COMMENTS',			'Comentarios');
define('_LISTS_TYPE',				'Tipo');


// member list
define('_LIST_MEMBER_NAME',			'Nome a amosar');
define('_LIST_MEMBER_RNAME',		'Nome real');
define('_LIST_MEMBER_ADMIN',		'Superadministrador? ');
define('_LIST_MEMBER_LOGIN',		'Podes rexistrarte? ');
define('_LIST_MEMBER_URL',			'Sitio web');

// banlist
define('_LIST_BAN_IPRANGE',			'Rango de IP');
define('_LIST_BAN_REASON',			'Razón');

// actionlist
define('_LIST_ACTION_MSG',			'Mensaxe');

// commentlist
define('_LIST_COMMENT_BANIP',		'Restricción de IP');
define('_LIST_COMMENT_WHO',			'Autor');
define('_LIST_COMMENT',				'Comentario');
define('_LIST_COMMENT_HOST',		'Host');

// itemlist
define('_LIST_ITEM_INFO',			'Información');
define('_LIST_ITEM_CONTENT',		'Título e texto');


// teamlist
define('_LIST_TEAM_ADMIN',			'Administrador ');
define('_LIST_TEAM_CHADMIN',		'Modificar administrador');

// edit comments
define('_EDITC_TITLE',				'Editar comentarios');
define('_EDITC_WHO',				'Autor');
define('_EDITC_HOST',				'Dende onde?');
define('_EDITC_WHEN',				'Cando?');
define('_EDITC_TEXT',				'Texto');
define('_EDITC_EDIT',				'Editar comentario');
define('_EDITC_MEMBER',				'membro');
define('_EDITC_NONMEMBER',			'non é membro');

// move item
define('_MOVE_TITLE',				'Mover a que bitácora?');
define('_MOVE_BTN',					'Cambiar entrada');

?>


