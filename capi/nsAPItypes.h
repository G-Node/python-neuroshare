///////////////////////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2003  Neuroshare Project                                                         
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// A copy of the GNU Lesser General Public License can be obtained by writing to:
//  Free Software Foundation, Inc.,
//  59 Temple Place, Suite 330,
//  Boston, MA  02111-1307
//  USA
//
// Contact information:
//  Angela Wang
//  CyberKinetics, Inc.,
//  391 G Chipeta Way
//  Salt Lake City,  UT  84108
//  USA
//  angela@bionictech.com
//
// Website:
//	www.neuroshare.org
//
// All other copyrights on this material are replaced by this license agreeement.
//
///////////////////////////////////////////////////////////////////////////////////////////////////
/* $Workfile: nsAPItypes.h $
*/
//
// File version  : 1.0
//
// Specification : based on Neuroshare API specification version 1.0
//
// Description   : This header file contains C declarations for constants, types,
//                 and structures defined in the Neuroshare API specification document
//
// Authors       : Shane Guillory, Angela Wang
//
/* $Date: 2/21/03 12:42p $
*/
//
/* $History: nsAPItypes.h $
// 
// *****************  Version 6  *****************
// User: Almut        Date: 2/21/03    Time: 12:42p
// Updated in $/Neuroshare/DLLTester
// These headers now conform to Neuroshare API Spec 1.0
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/21/03    Time: 11:45a
// Created in $/Neuroshare/nsNEVLibrary
// Version 1.0 Neuroshare Specifications
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/17/03    Time: 11:22a
// Created in $/Neuroshare/nsNEVLibrary
// Neuroshare API Ver 1.0 compliant header files
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/13/03    Time: 9:29a
// Created in $/Neuroshare/nsNEVLibrary
 * 
 * *****************  Version 5  *****************
 * User: Angela       Date: 1/14/03    Time: 9:42a
 * Updated in $/Neuroshare/nsNEVLibrary
 * Fixed location of brackets in structures
 * 
 * *****************  Version 4  *****************
 * User: Angela       Date: 1/10/03    Time: 12:13p
 * Updated in $/Neuroshare/nsNEVLibrary
 * Reword disclaimer
 * 
 * *****************  Version 3  *****************
 * User: Angela       Date: 1/09/03    Time: 12:14p
 * Updated in $/Neuroshare/nsNEVLibrary
 * Add copyright, disclaimer and file header

    v0.9b - Functions changed to use __stdcall calling convention for compatibility 
        with Visual Basic. Function prototype declarations also changed to
        all-capital versions of the neuroshare function names.
    v0.9b - First public release.. 
*/
///////////////////////////////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////////////////////////////////////////////////
//
//	Additional Remarks
// 
//  - The members of the Neuroshare API structures are defined on 4-byte boundaries.  Make sure to 
//    compile all with 4-byte or smaller alignement 
//
///////////////////////////////////////////////////////////////////////////////////////////////////

// Standard Include guards
#ifndef NSAPITYPES_H_INCLUDED
#define NSAPITYPES_H_INCLUDED


#define ns_LIBVERSION 0100  // version 01.00

///////////////////////////////////////////////////////////////////////////////////////////////////
//
// Fixed storage size definitions for declared variables
// (includes conditional testing so that there is no clash with win32 headers)
// 
///////////////////////////////////////////////////////////////////////////////////////////////////

#if defined(_MSC_VER)

  typedef signed __int8	   int8;
  typedef unsigned __int8  uint8;
  typedef signed __int16   int16;
  typedef unsigned __int16 uint16;
  typedef signed __int32   int32;
  typedef unsigned __int32 uint32;

  #pragma pack(push)
  #pragma pack(4) // specify 4-byte structure alignment

#else

  #include <stdint.h>

  typedef int8_t   int8;
  typedef uint8_t  uint8;
  typedef int16_t  int16;
  typedef uint16_t uint16;
  typedef int32_t  int32;
  typedef uint32_t uint32;


#endif


///////////////////////////////////////////////////////////////////////////////////////////////////
// 
// Library Return Code Definitions
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef	int32 ns_RESULT;
	
#define ns_OK          0  //Function Successful
#define	ns_LIBERROR	  -1  //Linked Library Error
#define	ns_TYPEERROR  -2  //Library unable to open file type
#define	ns_FILEERROR  -3  //File access or read Error
#define	ns_BADFILE    -4  //Invalid file handle passed to function
#define	ns_BADENTITY  -5  //Invalid or inappropriate entity identifier specified
#define	ns_BADSOURCE  -6  //Invalid source identifier specified
#define	ns_BADINDEX   -7  //Invalid entity index or index range specified
	
///////////////////////////////////////////////////////////////////////////////////////////////////
// 
// Definitions of constants and flags 
//
///////////////////////////////////////////////////////////////////////////////////////////////////

// Library description flags
#define ns_LIBRARY_DEBUG         0x01  // includes debug info linkage
#define ns_LIBRARY_MODIFIED      0x02  // file was patched or modified
#define ns_LIBRARY_PRERELEASE    0x04  // pre-release or beta version
#define ns_LIBRARY_SPECIALBUILD  0x08  // different from release version
#define ns_LIBRARY_MULTITHREADED 0x10  // library is multithread safe

//Definitions of Event Entity types
#define ns_EVENT_TEXT  0  // null-terminated ascii text string
#define ns_EVENT_CSV   1  // comma separated ascii text values
#define ns_EVENT_BYTE  2  // 8-bit value
#define ns_EVENT_WORD  3  // 16-bit value
#define ns_EVENT_DWORD 4  // 32-bit value
	
//Definitions of entity types in the structure ns_ENTITYINFO
#define ns_ENTITY_UNKNOWN     0	 // unknown entity type
#define ns_ENTITY_EVENT       1	 // Event entity
#define ns_ENTITY_ANALOG      2	 // Analog entity
#define ns_ENTITY_SEGMENT     3	 // Segment entity
#define ns_ENTITY_NEURALEVENT 4	 // Sorted Neural entity

//Flags used for locating data entries
#define ns_BEFORE  -1  // less than or equal to specified time	
#define ns_CLOSEST  0  // closest time 
#define ns_AFTER   +1  // greater than or equal to specified time	

///////////////////////////////////////////////////////////////////////////////////////////////////
// 
//			 DLL library version information functions
//
///////////////////////////////////////////////////////////////////////////////////////////////////

//File descriptor structure
typedef struct
{
	char szDescription[32];  // Text description of the file type or file family
	char szExtension[8];     // Extension used on PC, Linux, and Unix Platforms
	char szMacCodes[8];      // Application and Type Codes used on Mac Platforms
	char szMagicCode[16];    // Null-terminated code used at the file beginning
} ns_FILEDESC;

// Library information structure
typedef struct
{
	uint32 dwLibVersionMaj;    // Major version number of library
	uint32 dwLibVersionMin;	   // Minor version number of library
	uint32 dwAPIVersionMaj;    // Major version number of API
	uint32 dwAPIVersionMin;	   // Minor version number of API
	char   szDescription[64];  // Text description of the library
	char   szCreator[64];	   // Name of library creator
	uint32 dwTime_Year;        // Year of last modification date
	uint32 dwTime_Month;       // Month (0-11; January = 0) of last modification date
	uint32 dwTime_Day;         // Day of the month (1-31) of last modification date
	uint32 dwFlags;            // Additional library flags
	uint32 dwMaxFiles;         // Maximum number of files library can simultaneously open
	uint32 dwFileDescCount;    // Number of valid description entries in the following array
	ns_FILEDESC FileDesc[16];  // Text descriptor of files that the DLL can interpret
} ns_LIBRARYINFO;

// File information structure (the time of file creation should be reported in GMT)
typedef struct
{
	char   szFileType[32];         // Manufacturer's file type descriptor
	uint32 dwEntityCount;          // Number of entities in the data file.
	double dTimeStampResolution;   // Minimum timestamp resolution
	double dTimeSpan;              // Time span covered by the data file in seconds
	char   szAppName[64];          // Name of the application that created the file
	uint32 dwTime_Year;            // Year the file was created
	uint32 dwTime_Month;           // Month (0-11; January = 0)
	uint32 dwTime_DayofWeek;       // Day of the week (0-6; Sunday = 0)
	uint32 dwTime_Day;             // Day of the month (1-31)
	uint32 dwTime_Hour;            // Hour since midnight (0-23)
	uint32 dwTime_Min;             // Minute after the hour (0-59)
	uint32 dwTime_Sec;             // Seconds after the minute (0-59)
	uint32 dwTime_MilliSec;		   // Milliseconds after the second (0-1000)
	char   szFileComment[256];	   // Comments embedded in the source file
} ns_FILEINFO;

// General entity information structure
typedef struct
{
	char   szEntityLabel[32];  // Specifies the label or name of the entity
	uint32 dwEntityType;       // One of the ns_ENTITY_* types defined above
	uint32 dwItemCount;        // Number of data items for the specified entity in the file
} ns_ENTITYINFO;
	
// Event entity information structure
typedef struct
{
	uint32 dwEventType;      // One of the ns_EVENT_* types defined above
	uint32 dwMinDataLength;  // Minimum number of bytes that can be returned for an Event
	uint32 dwMaxDataLength;	 // Maximum number of bytes that can be returned for an Event
	char   szCSVDesc[128];   // Description of the data fields for CSV Event Entities
} ns_EVENTINFO;

// Analog information structure
typedef struct
{
	double	dSampleRate;           // The sampling rate in Hz used to digitize the analog values
	double	dMinVal;               // Minimum possible value of the input signal
	double	dMaxVal;               // Maximum possible value of the input signal
	char	szUnits[16];		   // Specifies the recording units of measurement
	double	dResolution;           // Minimum resolvable step (.0000305 for a +/-1V 16-bit ADC)  
	double	dLocationX;            // X coordinate in meters
	double	dLocationY;            // Y coordinate in meters
	double	dLocationZ;            // Z coordinate in meters
	double	dLocationUser;         // Additional position information (e.g. tetrode number)
	double	dHighFreqCorner;       // High frequency cutoff in Hz of the source signal filtering
	uint32	dwHighFreqOrder;       // Order of the filter used for high frequency cutoff
	char	szHighFilterType[16];  // Type of filter used for high frequency cutoff (text format)
	double	dLowFreqCorner;        // Low frequency cutoff in Hz of the source signal filtering
	uint32	dwLowFreqOrder;        // Order of the filter used for low frequency cutoff
	char	szLowFilterType[16];   // Type of filter used for low frequency cutoff (text format)
	char	szProbeInfo[128];      // Additional text information about the signal source
} ns_ANALOGINFO;
	
//Segment Information structure
typedef struct
{
	uint32 dwSourceCount;     // Number of sources in the Segment Entity, e.g. 4 for a tetrode
	uint32 dwMinSampleCount;  // Minimum number of samples in each Segment data item
	uint32 dwMaxSampleCount;  // Maximum number of samples in each Segment data item
	double dSampleRate;       // The sampling rate in Hz used to digitize source signals
	char   szUnits[32];       // Specifies the recording units of measurement
} ns_SEGMENTINFO;

// Segment source information structure
typedef struct
{
	double dMinVal;               // Minimum possible value of the input signal
	double dMaxVal;               // Maximum possible value of the input signal
	double dResolution;           // Minimum input step size that can be resolved
	double dSubSampleShift;       // Time diff btn timestamp and actual sampling time of source
	double dLocationX;            // X coordinate of source in meters
	double dLocationY;            // Y coordinate of source in meters
	double dLocationZ;            // Z coordinate of source in meters
	double dLocationUser;         // Additional position information (e.g tetrode number)
	double dHighFreqCorner;       // High frequency cutoff in Hz of the source signal filtering
	uint32 dwHighFreqOrder;       // Order of the filter used for high frequency cutoff
	char   szHighFilterType[16];  // Type of filter used for high frequency cutoff (text format)
	double dLowFreqCorner;		  // Low frequency cutoff in Hz of the source signal filtering
	uint32 dwLowFreqOrder;        // Order of the filter used for low frequency cutoff
	char   szLowFilterType[16];	  // Type of filter used for low frequency cutoff (text format)
	char   szProbeInfo[128];      // Additional text information about the signal source
} ns_SEGSOURCEINFO;

// Neural Information structure
typedef struct
{
	uint32 dwSourceEntityID;  // Optional ID number of a source entity
	uint32 dwSourceUnitID;    // Optional sorted unit ID number used in the source entity
	char   szProbeInfo[128];  // Additional probe text information or source entity label
} ns_NEURALINFO;

#if defined(_MSC_VER)
#  pragma pack(pop)
#endif

#endif
